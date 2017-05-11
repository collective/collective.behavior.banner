# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""
from collective.behavior.banner.testing import COLLECTIVE_BEHAVIOR_BANNER_FUNCTIONAL_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.app.testing import TEST_USER_ID
from plone.dexterity.fti import DexterityFTI
from plone.testing.z2 import Browser

import unittest


class TestFieldCase(unittest.TestCase):
    """Test integration of collective.behavior.banner into Plone."""

    layer = COLLECTIVE_BEHAVIOR_BANNER_FUNCTIONAL_TESTING

    behaviors = (
        'collective.behavior.banner.banner.IBanner',)
    portal_type = 'SomeDocument'

    def setUp(self):
        app = self.layer['app']
        self.portal = self.layer['portal']
        self.wf = api.portal.get_tool('portal_workflow')
        self.portal.acl_users._doAddUser('user_std', 'secret', ['Member'], [])
        self.portal_url = self.portal.absolute_url()
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        fti = DexterityFTI(self.portal_type)
        self.portal.portal_types._setObject(self.portal_type, fti)
        fti.klass = 'plone.dexterity.content.Item'
        fti.behaviors = self.behaviors
        api.content.create(
            container=self.portal,
            type=self.portal_type,
            id='doc1')
        setRoles(self.portal, TEST_USER_ID, ['Member'])
        import transaction

        transaction.commit()
        # Set up browser
        self.browser = Browser(app)
        self.browser.handleErrors = False
        self.browser.addHeader(
            'Authorization',
            'Basic {0}:{1}'.format(SITE_OWNER_NAME, SITE_OWNER_PASSWORD,)
        )

    def test_some_banner_fields(self):
        self.browser.open(self.portal_url + '/doc1/edit')
        self.assertTrue('Banner' in self.browser.contents)
        self.assertTrue('banner_fontcolor' in self.browser.contents)
        self.assertTrue('banner_linktext' in self.browser.contents)
