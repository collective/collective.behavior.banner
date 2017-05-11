# -*- coding: utf-8 -*-
from collective.behavior.banner.testing import COLLECTIVE_BEHAVIOR_BANNER_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.registry.interfaces import IRegistry
from Products.CMFPlone.interfaces import IResourceRegistry
from zope.component import getUtility

import unittest


CSS = (
    '++resource++collective.behavior.banner/banner.css',
    '++resource++collective.behavior.banner/slider.css',
)


class TestSetup(unittest.TestCase):
    """Test that collective.behavior.banner is properly installed."""

    layer = COLLECTIVE_BEHAVIOR_BANNER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.behavior.banner is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.behavior.banner'))

    def test_browserlayer(self):
        """Test that ICollectiveBannerLayer is registered."""
        from collective.behavior.banner.interfaces import (
            ICollectiveBannerLayer)
        from plone.browserlayer import utils
        self.assertIn(ICollectiveBannerLayer, utils.registered_layers())

    def test_cssregistry(self):
        bundles = getUtility(IRegistry).collectionOfInterface(
            IResourceRegistry, prefix='plone.resources')
        bundle = bundles['collective-behavior-banner']

        for id in CSS:
            self.assertIn(id, bundle.css, '{0} not installed'.format(id))

        self.assertIn(
            '++resource++collective.behavior.banner/responsiveslides.min.js',
            bundle.js)


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_BEHAVIOR_BANNER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.behavior.banner'])

    def test_product_uninstalled(self):
        """Test if collective.behavior.banner is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.behavior.banner'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveBannerLayer is removed."""
        from collective.behavior.banner.interfaces import (
            ICollectiveBannerLayer)
        from plone.browserlayer import utils
        self.assertNotIn(ICollectiveBannerLayer, utils.registered_layers())

    def test_cssregistry_removed(self):
        bundles = getUtility(IRegistry).collectionOfInterface(
            IResourceRegistry, prefix='plone.resources')
        self.assertNotIn(
            'collective-behavior-banner', bundles)
