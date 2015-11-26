# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.formwidget.contenttree import ContentTreeFieldWidget
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.namedfile import field as namedfile
from plone.supermodel import model
from z3c.relationfield.schema import RelationChoice
from zope import schema
from zope.component import adapts
from zope.interface import alsoProvides
from zope.interface import implements
from zope.interface import Invalid
from zope.interface.interface import invariant

from collective.behavior.banner import _


class IBanner(model.Schema):

    model.fieldset(
        'banner',
        label=u"Banner",
        fields=[
            'banner_hide',
            'banner_stop_inheriting',
            'banner_image',
            'banner_url',
            'banner_title',
            'banner_description',
            'banner_text',
            'banner_link',
            'banner_linktext',
            'banner_fontcolor',
        ]
    )

    banner_hide = schema.Bool(
        title=_(u"Hide banner"),
        description=_(u"This does not show the banner for this item."),
        default=False,
        required=False,
    )

    banner_stop_inheriting = schema.Bool(
        title=_(u"Do not inherit banner from parents"),
        description=_(
            u"This stops inheriting banners for this item and all children."),
        default=False,
        required=False,
    )

    banner_image = namedfile.NamedBlobImage(
        title=_(u"Banner Image"),
        description=u"",
        required=False,
    )

    banner_url = schema.URI(
        title=_(u'label_banner_url', default=u'Video URL'),
        description=u'''
        If you want the banner for this item to show a video, enter an
        external URL here.  YouTube and Vimeo are supported.  Note:
        You can either supply an image, or a video URL, not both.
        ''',
        required=False,
    )

    # @invariant
    # def validate_visual_content(data):
    #     """
    #     It is not allowed to add an image and an external url at the same time.
    #     """
    #     if data.banner_image and data.banner_url:
    #         raise Invalid(_(
    #             u'error_message_links',
    #             default=u'It\'s not possible to add an image and an '
    #                     u'external url at the same time')
    #         )

    banner_title = schema.TextLine(
        title=_(u"Banner Title"),
        description=u"",
        required=False,
    )

    banner_description = schema.Text(
        title=_(u"Banner Subtitle"),
        description=u"",
        required=False,
    )

    banner_text = RichText(
        title=_(u"Banner Text"),
        description=u"",
        required=False,
    )

    banner_link = RelationChoice(
        title=_(u"Banner Link"),
        description=u"",
        vocabulary="plone.app.vocabularies.Catalog",
        required=False,
    )

    banner_linktext = schema.TextLine(
        title=_(u"Link caption"),
        description=_(u'Caption for the link'),
        required=False,
    )

    banner_fontcolor = schema.TextLine(
        title=_(u"Fontcolor on the teaser"),
        description=_(u'Color for headings and texts as webcolor'),
        required=False,
    )


alsoProvides(IBanner, IFormFieldProvider)


class Banner(object):
    implements(IBanner)
    adapts(IDexterityContent)

    def __init__(self, context):
        self.context = context
