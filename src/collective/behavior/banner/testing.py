# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer

import collective.behavior.banner


class CollectiveBehaviorBannerLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=collective.behavior.banner)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.behavior.banner:default')


COLLECTIVE_BEHAVIOR_BANNER_FIXTURE = CollectiveBehaviorBannerLayer()


COLLECTIVE_BEHAVIOR_BANNER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_BEHAVIOR_BANNER_FIXTURE,),
    name='CollectiveBehaviorBannerLayer:IntegrationTesting'
)


COLLECTIVE_BEHAVIOR_BANNER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_BEHAVIOR_BANNER_FIXTURE,),
    name='CollectiveBehaviorBannerLayer:FunctionalTesting'
)


# COLLECTIVE_BEHAVIOR_BANNER_ACCEPTANCE_TESTING = FunctionalTesting(
#     bases=(
#         COLLECTIVE_BEHAVIOR_BANNER_FIXTURE,
#         REMOTE_LIBRARY_BUNDLE_FIXTURE,
#         z2.ZSERVER_FIXTURE
#     ),
#     name='CollectiveBehaviorBannerLayer:AcceptanceTesting'
# )
