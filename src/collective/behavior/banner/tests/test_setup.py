# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from collective.behavior.banner.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of collective.behavior.banner into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.behavior.banner is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('collective.behavior.banner'))

    def test_uninstall(self):
        """Test if collective.behavior.banner is cleanly uninstalled."""
        self.installer.uninstallProducts(['collective.behavior.banner'])
        self.assertFalse(self.installer.isProductInstalled('collective.behavior.banner'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that ICollective.behavior.BannerLayer is registered."""
        from collective.behavior.banner.interfaces import ICollectiveBannerLayer
        from plone.browserlayer import utils
        self.failUnless(ICollectiveBannerLayer in utils.registered_layers())
