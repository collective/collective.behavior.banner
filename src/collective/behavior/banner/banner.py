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
from zope.interface import implementer
from zope.interface import provider
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
    "1-3": "col-1-3",
    "1-2": "col-1-2",
    "2-3": "col-2-3",
}

# TODO: Add images (maybe: make it configurable or make it use content)
IMAGE_TEMPLATE_OPTIONS = SimpleVocabulary(
    [
        SimpleTerm("banner_1", "banner_1", _("Banner 1")),
        SimpleTerm("banner_2", "banner_2", _("Banner 2")),
        SimpleTerm("banner_3", "banner_3", _("Banner 3")),
        SimpleTerm("banner_4", "banner_4", _("Banner 4")),
    ]
)

BANNER_CIRCLE_COLORS = SimpleVocabulary(
    [
        SimpleTerm("f7b98f", "f7b98f", _("Verkehrsorange (hell)")),  # font-color: #000
        SimpleTerm("dc593c", "dc593c", _("Verkehrsrot (mittel)")),  # font-color: #000
        SimpleTerm("af0917", "af0917", _("Verkehrsrot (dunkel)")),  # font-color: #fff
        SimpleTerm("dea6a6", "dea6a6", _("BBF-Rot (hell)")),  # font-color: #000
        SimpleTerm("de5e73", "de5e73", _("Himbeerrot (mittel)")),  # font-color: #000
        SimpleTerm("abacd2", "abacd2", _("Violettblau (hell)")),  # font-color: #000
        SimpleTerm("b5b7b8", "b5b7b8", _("DIPF-Grau (hell)")),  # font-color: #000
        SimpleTerm("6794bc", "6794bc", _("Himmelblau (mittel)")),  # font-color: #000
        SimpleTerm("7dba61", "7dba61", _("Maigrün (mittel)")),  # font-color: #000
        SimpleTerm("7f9716", "7f9716", _("Gelbgrün (dunkel)")),  # font-color: #000
    ]
)


@provider(IFormFieldProvider)
class IBanner(model.Schema):

    model.fieldset(
        'banner',
        label=u'Banner',
        fields=[
            "banner_show_content_title",
            "banner_title_circle_color",
            'banner_image',
            "banner_image_template",
            'banner_alt',
            # 'banner_url',
            'banner_title',
            'banner_description',
            'banner_text',
            'banner_link',
            'banner_linktext',
            # 'banner_fontcolor',
            # 'banner_backgroundcolor',
            "banner_text_position",
            'banner_hide',
            'banner_stop_inheriting',
        ]
    )

    banner_show_content_title = schema.Bool(
        title=_("Show title in banner"),
        description=_("Display the context title in a circle overlaying the banner if the banner has no text."),
        default=False,
    )

    banner_title_circle_color = schema.Choice(
        title=_("Color of the circle with the context title"),
        description=_("Select a background color for the cirlce. Only valid when displaying the title in a circle in the banner"),
        vocabulary=BANNER_CIRCLE_COLORS,
        default="f7b98f",
        required=True,
    )

    banner_image = namedfile.NamedBlobImage(
        title=_(u'Banner Image'),
        description=_(u''),
        required=False,
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

    banner_image_template = schema.Choice(
        title=_("Neutral background image"),
        description=_("Select a neutral background image as a alternative to uploading a Banner Image."),
        vocabulary=IMAGE_TEMPLATE_OPTIONS,
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
        title=_("Text position"),
        description=_("Control the position of title and text. You can ignore this if there is no text"),
        vocabulary=TEXT_POSITION_OPTIONS,
        default="1-3",
        required=True,
    )


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
