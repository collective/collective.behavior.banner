# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from collective.behavior.teaser.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of collective.behavior.teaser into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.behavior.teaser is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('collective.behavior.teaser'))

    def test_uninstall(self):
        """Test if collective.behavior.teaser is cleanly uninstalled."""
        self.installer.uninstallProducts(['collective.behavior.teaser'])
        self.assertFalse(self.installer.isProductInstalled('collective.behavior.teaser'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that ICollective.behavior.teaserLayer is registered."""
        from collective.behavior.teaser.interfaces import ICollectiveTeaserLayer
        from plone.browserlayer import utils
        self.failUnless(ICollectiveTeaserLayer in utils.registered_layers())
