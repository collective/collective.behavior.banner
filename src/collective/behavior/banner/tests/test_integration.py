# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from collective.behavior.banner.testing import IntegrationTestCase
from plone import api


class TestIntegration(IntegrationTestCase):
    """Test integration of collective.behavior.banner into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_css_available(self):
        cssreg = getattr(self.portal, 'portal_css')
        stylesheets_ids = cssreg.getResourceIds()
        self.failUnless("++resource++collective.behavior.banner/slider.css" in stylesheets_ids)  # noqa
        self.failUnless("++resource++collective.behavior.banner/banner.css" in stylesheets_ids)  # noqa
