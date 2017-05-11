# -*- coding: UTF-8 -*-
from plone.app.registry.browser import controlpanel
from Products.CMFPlone import PloneMessageFactory as _
from zope import schema
from zope.interface import Interface


class IBannerSettingsSchema(Interface):

    types = schema.List(
        title=u'Types',
        description=_(u'Types displaying inherited banners'),
        required=False,
        value_type=schema.Choice(
            vocabulary='plone.app.vocabularies.ReallyUserFriendlyTypes',
        ),
        default=[
            'Collection',
            'Document',
            'Event',
            'File',
            'Folder',
            'Image',
            'Link',
            'News Item',
        ]
    )


class BannerSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IBannerSettingsSchema
    label = _(u'Banner settings')
    description = _(u'')

    def updateFields(self):
        super(BannerSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(BannerSettingsEditForm, self).updateWidgets()


class BannerSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = BannerSettingsEditForm
