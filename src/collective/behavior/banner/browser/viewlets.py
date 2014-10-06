# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from collective.behavior.banner.banner import IBanner
from collective.behavior.banner.browser.controlpanel import \
    IBannerSettingsSchema
from collective.behavior.banner.slider import ISlider
from plone.app.layout.navigation.interfaces import INavigationRoot
from plone.app.layout.viewlets import ViewletBase
from plone.registry.interfaces import IRegistry
from zope.component import getUtility

import random


class BannerViewlet(ViewletBase):
    """ A viewlet which renders the banner """

    banner_template = ViewPageTemplateFile('banner.pt')
    slider_template = ViewPageTemplateFile('slider.pt')

    def index(self):
        context = aq_inner(self.context)
        if ISlider.providedBy(context):
            if context.slider_relation and len(context.slider_relation) > 1:
                return self.slider_template()
        return self.banner_template()

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
        for item in context.aq_chain:
            if IBanner.providedBy(item):
                # we have a banner. check.
                if item.banner_stop_inheriting:
                    return False
                banner = self.banner(item)
                if banner:
                    return banner
            if INavigationRoot.providedBy(item):
                return False
            if item.portal_type not in types:
                return False

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
                banner['banner_linktext'] = to_obj.Title()
        if obj.banner_linktext:
            banner['banner_linktext'] = obj.banner_linktext
        if obj.banner_fontcolor:
            banner['banner_fontcolor'] = obj.banner_fontcolor
        return banner

    def random_banner(self):
        context = aq_inner(self.context)
        banners = []
        raw_banners = context.slider_relation
        for banner in raw_banners:
            banner = banner.to_object
            banners.append(self.banner(banner))

        self.scroll = len(banners) > 1

        random.shuffle(banners)
        return banners
