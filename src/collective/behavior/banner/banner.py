# -*- coding: utf-8 -*-
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.directives import form
from plone.app.textfield import RichText
from plone.namedfile import field as namedfile
from plone.supermodel import model
from zope import schema
from zope.component import adapts
from zope.interface import alsoProvides, implements
from plone.formwidget.contenttree import ObjPathSourceBinder
from z3c.relationfield.schema import RelationChoice

from collective.behavior.banner import _


class IBanner(model.Schema):

    form.fieldset(
        'banner',
        label=u"Banner",
        fields=[
            'banner_hide',
            'banner_stop_inheriting',
            'banner_image',
            'banner_title',
            'banner_description',
            'banner_text',
            'banner_link',
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
        source=ObjPathSourceBinder(),
        required=False,
    )

alsoProvides(IBanner, IFormFieldProvider)


class Banner(object):
    implements(IBanner)
    adapts(IDexterityContent)

    def __init__(self, context):
        self.context = context
