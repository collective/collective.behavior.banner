# -*- coding: utf-8 -*-
from collective.behavior.banner import _
from collective.behavior.banner.banner import IBanner
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform import directives as form
from plone.formwidget.contenttree import MultiContentTreeFieldWidget
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.supermodel import model
from z3c.relationfield.schema import RelationChoice, RelationList
from zope.component import adapts
from zope.interface import alsoProvides, implements


class ISlider(model.Schema):

    model.fieldset(
        'slider',
        label=u"Slider",
        fields=[
            'slider_relation',
        ]
    )

    form.widget(
        slider_relation=MultiContentTreeFieldWidget)
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
