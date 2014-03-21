# -*- coding: UTF-8 -*-
from Products.CMFPlone import PloneMessageFactory as _
from plone.app.registry.browser import controlpanel
from zope import schema
from zope.interface import Interface


class ITeaserSettingsSchema(Interface):

    types = schema.List(
        title=u'Types',
        description=_(u'Types displaying inherited teasers'),
        required=False,
        value_type=schema.Choice(
            vocabulary='plone.app.vocabularies.ReallyUserFriendlyTypes',
        ),
        default=[
            "Collection",
            "Document",
            "Event",
            "File",
            "Folder",
            "Image",
            "Link",
            "News Item",
        ]
    )


class TeaserSettingsEditForm(controlpanel.RegistryEditForm):

    schema = ITeaserSettingsSchema
    label = _(u"Teaser settings")
    description = _(u"""""")

    def updateFields(self):
        super(TeaserSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(TeaserSettingsEditForm, self).updateWidgets()


class TeaserSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = TeaserSettingsEditForm
