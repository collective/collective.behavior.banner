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

from collective.behavior.teaser import _


class ITeaser(model.Schema):

    form.fieldset(
        'teaser',
        label=u"Teaser",
        fields=[
            'teaser_display',
            'teaser_inherit',
            'teaser_image',
            'teaser_title',
            'teaser_description',
            'teaser_text',
        ]
    )

    teaser_display = schema.Bool(
        title=_(u"Show Teaser"),
        description=u"",
        default=True,
        required=False,
    )

    teaser_inherit = schema.Bool(
        title=_(u"Inherit Teaser from parent folder"),
        description=u"",
        default=True,
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


alsoProvides(ITeaser, IFormFieldProvider)


class Teaser(object):
    implements(ITeaser)
    adapts(IDexterityContent)

    def __init__(self, context):
        self.context = context
