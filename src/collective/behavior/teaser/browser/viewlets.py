# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from collective.behavior.teaser.browser.controlpanel import \
    ITeaserSettingsSchema
from collective.behavior.teaser.teaser import ITeaser
from plone.app.layout.navigation.interfaces import INavigationRoot
from plone.app.layout.viewlets import ViewletBase
from plone.registry.interfaces import IRegistry
from zope.component import getUtility


class TeaserViewlet(ViewletBase):
    """ A viewlet which renders the teaser """

    def find_teaser(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ITeaserSettingsSchema)
        types = settings.types
        context = aq_inner(self.context)
        # first handle the obj itself
        if ITeaser.providedBy(context):
            if context.teaser_hide:
                return False
            teaser = self.teaser(context)
            if teaser:
                return teaser
            if context.teaser_stop_inheriting:
                return False
            # if all the fields are empty and inheriting is not stopped
        if context.portal_type not in types:
            return False
        context = context.__parent__

        # we walk up the path
        while True:
            if ITeaser.providedBy(context):
                # we have a teaser. check.
                if context.teaser_stop_inheriting:
                    return False
                teaser = self.teaser(context)
                if teaser:
                    return teaser
            if INavigationRoot.providedBy(context):
                return False
            if context.portal_type not in types:
                return False
            context = context.__parent__

        return False

    def teaser(self, obj):
        """ return teaser of this object """
        teaser = {}
        if getattr(obj, 'teaser_image', False):
            teaser['teaser_image'] = '%s/@@images/teaser_image' \
                % obj.absolute_url()
        if obj.teaser_title:
            teaser['teaser_title'] = obj.teaser_title
        if obj.teaser_description:
            teaser['teaser_description'] = obj.teaser_description
        if obj.teaser_text:
            teaser['teaser_text'] = obj.teaser_text.output
        return teaser
