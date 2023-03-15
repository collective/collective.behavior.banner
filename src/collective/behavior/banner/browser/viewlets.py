# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from collective.behavior.banner.banner import (
    CSS_CLASS_MAPPING,
    IBanner,
)
from collective.behavior.banner.slider import ISlider
from plone import api
from plone.app.layout.navigation.interfaces import INavigationRoot
from plone.app.layout.viewlets import ViewletBase
from Products.CMFPlone.browser.ploneview import Plone
from Products.CMFPlone.defaultpage import get_default_page
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from six.moves.urllib.parse import urlparse

import random

# Values a banner can have without being counted a banner.
IGNORE_KEYS = ['banner_obj', 'textblock_css_class', 'banner_size']


class BannerViewlet(ViewletBase):
    """A viewlet which renders the banner"""

    banner_template = ViewPageTemplateFile("banner.pt")
    slider_template = ViewPageTemplateFile("slider.pt")

    def render(self):
        if "@@edit" in self.request.steps:
            return ""
        return self.index()

    def index(self):
        context = aq_inner(self.context)
        if ISlider.providedBy(context):
            if context.slider_relation and len(context.slider_relation) > 1:
                return self.slider_template()
        return self.banner_template()

    def find_banner(self):  # noqa: C901
        types = api.portal.get_registry_record(
            "collective.behavior.banner.browser.controlpanel.IBannerSettingsSchema.types"
        )  # noqa: E501
        context = aq_inner(self.context)
        # first handle the obj itself
        if IBanner.providedBy(context):
            if context.banner_hide:
                return False
            banner = self.banner(context)
            config_keys = [key for key in banner.keys() if key not in IGNORE_KEYS]
            if config_keys:
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
                config_keys = [key for key in banner.keys() if key not in IGNORE_KEYS]
                if config_keys:
                    return banner
            if INavigationRoot.providedBy(item):
                default_page = get_default_page(item)
                if default_page:
                    default_page = item[default_page]
                    if IBanner.providedBy(default_page):
                        banner = self.banner(default_page)
                        if banner:
                            return banner
                return False
            if item.portal_type not in types:
                return False

        return False

    def banner_scale(self):
        return api.portal.get_registry_record(
            "collective.behavior.banner.browser.controlpanel.IBannerSettingsSchema.banner_scale",  # noqa: E501
            default="preview",
        )

    def banner(self, obj):  # noqa: C901
        """return banner of this object"""
        banner = {}
        if getattr(obj, "banner_image", False):
            banner["banner_image"] = "{0}/@@images/banner_image".format(
                obj.absolute_url())
            banner["banner_alt"] = getattr(obj, "banner_alt", None)
        elif obj.banner_image_template:
            filename = obj.banner_image_template
            banner["banner_image_template"] = self.context.absolute_url() + "/++resource++collective.behavior.banner/" + filename
        else:
            # no image => no banner
            return banner

        if obj.banner_title:
            banner["banner_title"] = obj.banner_title
        if obj.banner_description:
            crop = Plone(self.context, self.request).cropText
            banner["banner_description"] = crop(obj.banner_description, 400)
        if obj.banner_text and obj.banner_text.output.strip():
            banner["banner_text"] = obj.banner_text.output.strip()
        if obj.banner_link:
            to_obj = obj.banner_link.to_object
            if to_obj:
                banner["banner_link"] = to_obj.absolute_url()
                banner["banner_linktext"] = to_obj.Title()
        if obj.banner_linktext:
            banner["banner_linktext"] = obj.banner_linktext

        banner_text_position = getattr(obj, "banner_text_position", None)
        banner["textblock_css_class"] = CSS_CLASS_MAPPING.get(banner_text_position, "")
        banner["banner_size"] = obj.banner_size
        banner["banner_obj"] = obj
        return banner

    def random_banner(self):
        context = aq_inner(self.context)
        banners = []
        raw_banners = context.slider_relation
        for raw_banner in raw_banners:
            obj = raw_banner.to_object
            banner = self.banner(obj)
            if banner:
                banners.append(banner)
        self.scroll = len(banners) > 1
        return banners

    def getVideoEmbedMarkup(self, url):
        """Build an iframe from a YouTube or Vimeo share url"""
        # https://www.youtube.com/watch?v=Q6qYdJuWB6w
        YOUTUBE_TEMPLATE = """
            <iframe
                width="660"
                height="495"
                src="//www.youtube-nocookie.com/embed/{1}?showinfo=0"
                frameborder="0"
                allowfullscreen>
            </iframe>
        """
        # https://vimeo.com/75721023
        VIMEO_TEMPLATE = """
            <iframe
                src="//player.vimeo.com/video/{0}?title=0&amp;byline=0&amp;portrait=0"
                width="660"
                height="371"
                frameborder="0"
                webkitallowfullscreen
                mozallowfullscreen
                allowfullscreen>
            </iframe>
        """
        try:
            parsed = urlparse(url)
        except AttributeError:
            return ""
        path = parsed.path.replace("/", "")
        videoId = parsed.query.replace("v=", "")
        if "youtube" in parsed.netloc:
            template = YOUTUBE_TEMPLATE
        elif "vimeo" in parsed.netloc:
            template = VIMEO_TEMPLATE
        else:
            return ""
        # It so happens that path is needed by the Vimeo format,
        # while videoId is needed by the Youtube format, so only one
        # of the variables will have a useful value, depending on the player.
        # Each template will use the argument it cares about and ignore the
        # other.
        return template.format(path, videoId)

    def show_content_title(self):
        """The value from the field banner_show_content_title is taken
        from the context not from the inherited banner!
        """
        return getattr(self.context, "banner_show_content_title", None)

    def circle_color(self):
        """The value from the field banner_title_circle_color is taken
        from the context not from the inherited banner!
        """
        color = getattr(self.context, "banner_title_circle_color", None)
        if color and color != "None":
            return color
