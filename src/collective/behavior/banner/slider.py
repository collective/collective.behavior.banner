# -*- coding: utf-8 -*-
from collective.behavior.banner import _
from collective.behavior.banner.banner import IBanner
from plone.app.z3cform.widget import RelatedItemsFieldWidget
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform import directives as form
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.supermodel import model
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from zope.component import adapts
from zope.interface import alsoProvides
from zope.interface import implements


class ISlider(model.Schema):

    model.fieldset(
        'slider',
        label=u"Slider",
        fields=[
            'slider_relation',
        ]
    )

    form.widget('slider_relation', RelatedItemsFieldWidget,
                vocabulary='plone.app.vocabularies.Catalog')
    slider_relation = RelationList(
        title=_(u"Slider Banners"),
        description=_(u"These banners will be used in the slider"),
        default=[],
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
