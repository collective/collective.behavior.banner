# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.behavior.banner.testing import COLLECTIVE_BEHAVIOR_BANNER_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


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
