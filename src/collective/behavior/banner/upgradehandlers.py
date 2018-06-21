# -*- coding: utf-8 -*-

from Products.CMFPlone import PloneMessageFactory as _
from plone.registry import field
from plone.registry import Record
from plone.registry.interfaces import IRegistry
from zope.component import getUtility


def upgrade_registry_for_banner_scale(context):
    key_id = 'collective.behavior.banner.browser.controlpanel.IBannerSettingsSchema.banner_scale'
    registry = getUtility(IRegistry)
    records = registry.records
    if key_id in records:
        return

    record = Record(
        field.Choice(
            title=_(u'Banner scale'),
            description=_(u'Scale at which banner images are displayed'),
            required=True,
            vocabulary='collective.behavior.banner.all_sizes',
            default='preview'),
        value='preview')
    records[key_id] = record
