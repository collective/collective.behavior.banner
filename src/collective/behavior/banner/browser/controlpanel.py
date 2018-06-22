# -*- coding: UTF-8 -*-
from plone.app.imaging.utils import getAllowedSizes
from plone.app.registry.browser import controlpanel
from Products.CMFPlone import PloneMessageFactory as _
from zope import schema
from zope.interface import implementer
from zope.interface import Interface
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary


@implementer(IVocabularyFactory)
class SizesVocabulary(object):

    def __call__(self, context):
        allowed_sizes = getAllowedSizes()
        size_names = allowed_sizes and allowed_sizes.keys() or []
        return SimpleVocabulary.fromValues(size_names)


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

    banner_scale = schema.Choice(
        title=_(u'Banner scale'),
        description=_(u'Scale at which banner images are displayed'),
        required=True,
        default='preview',
        vocabulary='collective.behavior.banner.all_sizes',
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
