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

from collective.behavior.teaser import _


class ITeaser(model.Schema):

    form.fieldset(
        'teaser',
        label=u"Teaser",
        fields=[
            'teaser_hide',
            'teaser_stop_inheriting',
            'teaser_image',
            'teaser_title',
            'teaser_description',
            'teaser_text',
            'teaser_link',
        ]
    )

    teaser_hide = schema.Bool(
        title=_(u"Hide Teaser"),
        description=_(u"This does not show the teaser for this item."),
        default=False,
        required=False,
    )

    teaser_stop_inheriting = schema.Bool(
        title=_(u"Do not inherit Teaser from parents"),
        description=_(
            u"This stops inheriting teasers for this item and all children."),
        default=False,
        required=False,
    )

    teaser_image = namedfile.NamedBlobImage(
        title=_(u"Teaser Image"),
        description=u"",
        required=False,
    )

    teaser_title = schema.TextLine(
        title=_(u"Teaser Title"),
        description=u"",
        required=False,
    )

    teaser_description = schema.Text(
        title=_(u"Teaser Subtitle"),
        description=u"",
        required=False,
    )

    teaser_text = RichText(
        title=_(u"Teaser Text"),
        description=u"",
        required=False,
    )

    teaser_link = RelationChoice(
        title=_(u"Teaser Link"),
        description=u"",
        source=ObjPathSourceBinder(),
        required=False,
    )

alsoProvides(ITeaser, IFormFieldProvider)


class Teaser(object):
    implements(ITeaser)
    adapts(IDexterityContent)

    def __init__(self, context):
        self.context = context
