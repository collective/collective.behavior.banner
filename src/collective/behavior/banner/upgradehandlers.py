# -*- coding: utf-8 -*-

from plone.registry import field
from plone.registry import Record
from plone.registry.interfaces import IRegistry
from Products.CMFPlone import PloneMessageFactory as _
from zope.component import getUtility


def upgrade_registry_for_banner_scale(context):
    key_id = "collective.behavior.banner.browser.controlpanel.IBannerSettingsSchema.banner_scale"  # noqa: E501
    registry = getUtility(IRegistry)
    records = registry.records
    if key_id in records:
        return

    record = Record(
        field.Choice(
            title=_("Banner scale"),
            description=_("Scale at which banner images are displayed"),
            required=True,
            vocabulary="collective.behavior.banner.all_sizes",
            default="preview",
        ),
        value="preview",
    )
    records[key_id] = record
