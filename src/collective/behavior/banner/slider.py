# -*- coding: utf-8 -*-
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.directives import form
from plone.supermodel import model
from zope import schema
from zope.component import adapts
from zope.interface import alsoProvides, implements
from plone.formwidget.contenttree import ObjPathSourceBinder
from z3c.relationfield.schema import RelationChoice, RelationList

from collective.behavior.banner.banner import IBanner

from collective.behavior.banner import _


class ISlider(model.Schema):

    form.fieldset(
        'slider',
        label=u"Slider",
        fields=[
            'slider_relation',
        ]
    )

    slider_relation = RelationList(
            title=_(u"Slider Banners"),
            description=_(u"This banners will be used for the slider"),
            value_type=RelationChoice(
                title=_(u'Target'),
                source=ObjPathSourceBinder(
                  object_provides=IBanner.__identifier__,
                )),
            required=False,
    )

alsoProvides(ISlider, IFormFieldProvider)


class Slider(object):
    implements(ISlider)
    adapts(IDexterityContent)

    def __init__(self, context):
        self.context = context
