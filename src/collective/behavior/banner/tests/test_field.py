# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from collective.behavior.banner.testing import IntegrationTestCase
from plone import api


class TestFieldCase(IntegrationTestCase):
    """Test integration of collective.behavior.banner into Plone."""

    def test_field_available(self):
        obj = createContentInContainer(
            self.portal,
            'dexterity_content_with_banner_behaviour',
            title=u"Test folder",
        )

        # first test newly created document
        self.failUnless('carouselprovider' in new_obj.Schema().keys())
        # now test the folder
        self.failUnless('carouselprovider' in self.folder.Schema().keys())

