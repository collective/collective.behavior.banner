# -*- coding: utf-8 -*-
from collective.behavior.banner import _
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.indexer.decorator import indexer
from plone.namedfile import field as namedfile
from plone.supermodel import model
from z3c.form.browser.radio import RadioFieldWidget
from z3c.relationfield.schema import RelationChoice
from zope import schema
from zope.component import adapter
from zope.interface import alsoProvides
from zope.interface import implementer
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm


TEXT_POSITION_OPTIONS = SimpleVocabulary(
    [
        SimpleTerm("1-3", "1-3", _("1/3")),
        SimpleTerm("1-2", "1-2", _("Middle")),
        SimpleTerm("2-3", "2-3", _("2/3")),
    ]
)

# TODO: Use usefull css-classes here :)
CSS_CLASS_MAPPING = {
    "1-3": "col-md-4 ",
    "1-2": "col-md-4 offset-md-4",
    "2-3": "col-md-4 offset-md-8",
}

# TODO: Add images (maybe: make it configurable or make it use content)
IMAGE_MAPPING = {
    "Circles": "foo",
    "Grid": "bar",
    "Swirlies": "baz",
}

BANNER_CIRCLE_COLORS = {
    "Red": "red",
    "Green": "green",
    "Blue": "blue",
}


class IBanner(model.Schema):

    model.fieldset(
        'banner',
        label=u'Banner',
        fields=[
            'banner_hide',
            'banner_stop_inheriting',
            'banner_image',
            'banner_alt',
            # 'banner_url',
            'banner_title',
            'banner_description',
            'banner_text',
            'banner_link',
            'banner_linktext',
            # 'banner_fontcolor',
            # 'banner_backgroundcolor',
            "banner_image_template",
            "banner_text_position",
            "banner_show_content_title",
            "banner_title_circle_color",
        ]
    )

    banner_hide = schema.Bool(
        title=_(u'Hide banner'),
        description=_(u'This does not show the banner for this item.'),
        default=False,
        required=False,
    )

    banner_stop_inheriting = schema.Bool(
        title=_(u'Do not inherit banner from parents'),
        description=_(
            u'This stops inheriting banners for this item and all children.'),
        default=False,
        required=False,
    )

    banner_image = namedfile.NamedBlobImage(
        title=_(u'Banner Image'),
        description=u'',
        required=False,
    )

    banner_image_template = schema.Choice(
        title="Neutral background image",
        description="Select a neutral background image as a alternative to uploading a Banner Image.",
        values=IMAGE_MAPPING.keys(),
        required=False,
    )

    banner_alt = schema.TextLine(
        title=_(u'Banner image alt tag'),
        description=u'',
        required=False,
    )

    # banner_url = schema.URI(
    #     title=_(u'label_banner_url', default=u'Video URL'),
    #     description=u'''
    #     If you want the banner for this item to show a video, enter an
    #     external URL here.  YouTube and Vimeo are supported.  Note:
    #     You can either supply an image, or a video URL, not both.
    #     ''',
    #     required=False,
    # )

    banner_title = schema.TextLine(
        title=_(u'Banner Title'),
        description=u'',
        required=False,
    )

    banner_description = schema.Text(
        title=_(u'Banner Subtitle'),
        description=u'',
        required=False,
    )

    banner_text = RichText(
        title=_(u'Banner Text'),
        description=u'',
        required=False,
    )

    banner_link = RelationChoice(
        title=_(u'Banner Link'),
        description=u'',
        vocabulary='plone.app.vocabularies.Catalog',
        required=False,
    )

    banner_linktext = schema.TextLine(
        title=_(u'Link caption'),
        description=_(u'Caption for the link'),
        required=False,
    )

    # banner_fontcolor = schema.TextLine(
    #     title=_(u'Fontcolor on the teaser'),
    #     description=_(u'Color for headings and texts as webcolor'),
    #     required=False,
    # )

    # banner_backgroundcolor = schema.TextLine(
    #     title=_(u'Background color'),
    #     description=_(u'Background color on the banner'),
    #     required=False,
    # )

    directives.widget(banner_text_position=RadioFieldWidget)
    banner_text_position = schema.Choice(
        title="Text position",
        description="Control the position of title and text. You can ignore this if there is no text",
        vocabulary=TEXT_POSITION_OPTIONS,
        default="1-3",
        required=True,
    )

    banner_show_content_title = schema.Bool(
        title="Show title in banner",
        description="Display the context title in a circle overlaying the banner if the banner has no text.",
        default=True,
    )

    banner_title_circle_color = schema.Choice(
        title="Color of the circle with the context title",
        description="Select a background color for the cirlce. Only valid when displaying the title in a circle in the banner",
        values=BANNER_CIRCLE_COLORS.keys(),
        default=list(BANNER_CIRCLE_COLORS.keys())[0],
        required=True,
    )

alsoProvides(IBanner, IFormFieldProvider)


@implementer(IBanner)
@adapter(IDexterityContent)
class Banner(object):

    def __init__(self, context):
        self.context = context


@indexer(IBanner)
def has_image(object, **kw):
    return (object.banner_image
            or object.banner_title
            or object.banner_description
            or object.banner_text
            or object.banner_link
            or object.banner_image_template
            )
