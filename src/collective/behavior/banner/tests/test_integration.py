# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from collective.behavior.banner.testing import COLLECTIVE_BEHAVIOR_BANNER_INTEGRATION_TESTING  # noqa
from plone import api
import unittest


class TestIntegration(unittest.TestCase):
    """Test integration of collective.behavior.banner into Plone."""

    layer = COLLECTIVE_BEHAVIOR_BANNER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_css_available(self):
        cssreg = getattr(self.portal, 'portal_css')
        stylesheets_ids = cssreg.getResourceIds()
        self.assertNotIn(
            "++resource++collective.behavior.banner/slider.css",
            stylesheets_ids)
        self.assertNotIn(
            "++resource++collective.behavior.banner/banner.css",
            stylesheets_ids)
