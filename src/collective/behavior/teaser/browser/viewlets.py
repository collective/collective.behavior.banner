# -*- coding: utf-8 -*-
from Acquisition import aq_inner
from Acquisition import aq_parent
from dgbbw.site.behaviors.teaser import ITeaser
from plone.app.layout.viewlets import ViewletBase
from zope.component import getMultiAdapter
from plone.app.layout.navigation.interfaces import INavigationRoot


class TeaserViewlet(ViewletBase):
    """ A viewlet which renders the teaser """

    # def update(self):
    #     self.available = True if self.context.teaser_image else False

    def teaser(self):
        teaser = {}
        obj = aq_inner(self.context)
        while not hasattr(obj, 'teaser_display'):
            if INavigationRoot.providedBy(obj):
                return False

            if obj.teaser_display:
                break

            if obj.teaser_inherit:
                obj = obj.aq_parent

        if obj.teaser_display is False:
            return False

        if getattr(obj, 'teaser_image', False):
            teaser['teaser_image'] = '%s/@@images/teaser_image' % obj.absolute_url()

        if obj.teaser_title:
            teaser['teaser_title'] = obj.teaser_title
        if obj.teaser_description:
            teaser['teaser_description'] = obj.teaser_description
        if obj.teaser_text:
            teaser['teaser_text'] = obj.teaser_text.output

        return teaser

        # context = aq_inner(self.context)
        # if not getattr(context, 'teaser_header', None):
        #     context_state = getMultiAdapter(
        #         (context, self.request), name=u"plone_context_state")
        #     if not context_state.is_default_page():
        #         return False
        #     else:
        #         context = aq_parent(context)
        #         if not getattr(context, 'teaser_header', None):
        #             return False
        # result = {}
        # result['teaser_header'] = context.teaser_header
        # result['teaser_subtitle'] = context.teaser_subtitle
        # body = context.teaser_body
        # result['teaser_body'] = body.output if body else False
        # result['has_image'] = getattr(context, 'image', False)
        # result['teaser_base_url'] = context.absolute_url()
        # return result
