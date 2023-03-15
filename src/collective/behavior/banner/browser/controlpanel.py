# -*- coding: UTF-8 -*-
from plone.app.registry.browser import controlpanel
from Products.CMFPlone import PloneMessageFactory as _
from zope import schema
from zope.interface import implementer
from zope.interface import Interface
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary


try:
    from Products.CMFPlone.utils import getAllowedSizes
except ImportError:
    from plone.app.imaging.utils import getAllowedSizes


@implementer(IVocabularyFactory)
class SizesVocabulary(object):
    def __call__(self, context):
        allowed_sizes = getAllowedSizes()
        size_names = allowed_sizes and list(allowed_sizes.keys()) or []
        return SimpleVocabulary.fromValues(size_names)


class IBannerSettingsSchema(Interface):

    types = schema.List(
        title="Types",
        description=_("Types displaying inherited banners"),
        required=False,
        value_type=schema.Choice(
            vocabulary="plone.app.vocabularies.ReallyUserFriendlyTypes",
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
        ],
    )

    banner_scale = schema.Choice(
        title=_("Banner scale"),
        description=_("Scale at which banner images are displayed"),
        required=True,
        default="preview",
        vocabulary="collective.behavior.banner.all_sizes",
    )


class BannerSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IBannerSettingsSchema
    label = _("Banner settings")
    description = ""


class BannerSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = BannerSettingsEditForm
