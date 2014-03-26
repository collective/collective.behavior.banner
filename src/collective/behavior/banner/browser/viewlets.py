# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from collective.behavior.banner.browser.controlpanel import \
    IBannerSettingsSchema
from collective.behavior.banner.banner import IBanner
from plone.app.layout.navigation.interfaces import INavigationRoot
from plone.app.layout.viewlets import ViewletBase
from plone.registry.interfaces import IRegistry
from zope.component import getUtility


class BannerViewlet(ViewletBase):
    """ A viewlet which renders the banner """

    def find_banner(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IBannerSettingsSchema)
        types = settings.types
        context = aq_inner(self.context)
        # first handle the obj itself
        if IBanner.providedBy(context):
            if context.banner_hide:
                return False
            banner = self.banner(context)
            if banner:
                return banner
            if context.banner_stop_inheriting:
                return False
            # if all the fields are empty and inheriting is not stopped
        if context.portal_type not in types:
            return False
        context = context.__parent__

        # we walk up the path
        while True:
            if IBanner.providedBy(context):
                # we have a banner. check.
                if context.banner_stop_inheriting:
                    return False
                banner = self.banner(context)
                if banner:
                    return banner
            if INavigationRoot.providedBy(context):
                return False
            if context.portal_type not in types:
                return False
            context = context.__parent__

        return False

    def banner(self, obj):
        """ return banner of this object """
        banner = {}
        if getattr(obj, 'banner_image', False):
            banner['banner_image'] = '%s/@@images/banner_image' \
                % obj.absolute_url()
        if obj.banner_title:
            banner['banner_title'] = obj.banner_title
        if obj.banner_description:
            banner['banner_description'] = obj.banner_description
        if obj.banner_text:
            banner['banner_text'] = obj.banner_text.output
        if obj.banner_link:
            to_obj = obj.banner_link.to_object
            if to_obj:
                banner['banner_link'] = to_obj.absolute_url()
                banner['banner_link_title'] = to_obj.Title()
        return banner
