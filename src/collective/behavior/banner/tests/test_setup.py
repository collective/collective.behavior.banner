# -*- coding: utf-8 -*-
from collective.behavior.banner.testing import (  # noqa: E501
    COLLECTIVE_BEHAVIOR_BANNER_INTEGRATION_TESTING,
)
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.base.interfaces.resources import IBundleRegistry
from plone.base.utils import get_installer
from plone.registry.interfaces import IRegistry
from zope.component import getUtility

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.behavior.banner is properly installed."""

    layer = COLLECTIVE_BEHAVIOR_BANNER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])

    def test_product_installed(self):
        """Test if collective.behavior.banner is installed."""
        self.assertTrue(
            self.installer.is_product_installed("collective.behavior.banner")
        )

    def test_browserlayer(self):
        """Test that ICollectiveBannerLayer is registered."""
        from collective.behavior.banner.interfaces import ICollectiveBannerLayer
        from plone.browserlayer import utils

        self.assertIn(ICollectiveBannerLayer, utils.registered_layers())

    def test_cssregistry(self):
        bundles = getUtility(IRegistry).collectionOfInterface(
            IBundleRegistry, prefix="plone.bundles"
        )
        self.assertIn("responsiveslides", bundles)
        self.assertIn("collective_behavior_banner", bundles)

        bundle = bundles["responsiveslides"]

        self.assertIn(
            "++plone++collective.behavior.banner/responsiveslides.css",
            bundle.csscompilation,
            "{0} not installed".format(id),
        )
        self.assertIn(
            "++plone++collective.behavior.banner/responsiveslides.min.js",
            bundle.jscompilation,
        )


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_BEHAVIOR_BANNER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("collective.behavior.banner")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if collective.behavior.banner is cleanly uninstalled."""
        self.assertFalse(
            self.installer.is_product_installed("collective.behavior.banner")
        )

    def test_browserlayer_removed(self):
        """Test that ICollectiveBannerLayer is removed."""
        from collective.behavior.banner.interfaces import ICollectiveBannerLayer
        from plone.browserlayer import utils

        self.assertNotIn(ICollectiveBannerLayer, utils.registered_layers())

    def test_cssregistry_removed(self):
        bundles = getUtility(IRegistry).collectionOfInterface(
            IBundleRegistry, prefix="plone.bundles"
        )
        self.assertNotIn("collective_behavior_banner", bundles)
        self.assertNotIn("responsiveslides", bundles)
