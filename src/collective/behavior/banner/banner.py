# -*- coding: utf-8 -*-
from collective.behavior.banner import _
from plone.app.textfield import RichText
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.indexer.decorator import indexer
from plone.namedfile import field as namedfile
from plone.supermodel import model
from z3c.relationfield.schema import RelationChoice
from zope import schema
from zope.component import adapter
from zope.interface import alsoProvides
from zope.interface import implementer


class IBanner(model.Schema):

    model.fieldset(
        "banner",
        label="Banner",
        fields=[
            "banner_hide",
            "banner_stop_inheriting",
            "banner_image",
            "banner_alt",
            "banner_url",
            "banner_title",
            "banner_description",
            "banner_text",
            "banner_link",
            "banner_linktext",
            "banner_fontcolor",
            "banner_backgroundcolor",
        ],
    )

    banner_hide = schema.Bool(
        title=_("Hide banner"),
        description=_("This does not show the banner for this item."),
        default=False,
        required=False,
    )

    banner_stop_inheriting = schema.Bool(
        title=_("Do not inherit banner from parents"),
        description=_("This stops inheriting banners for this item and all children."),
        default=False,
        required=False,
    )

    banner_image = namedfile.NamedBlobImage(
        title=_("Banner Image"),
        description="",
        required=False,
    )

    banner_alt = schema.TextLine(
        title=_("Banner image alt tag"),
        description="",
        required=False,
    )

    banner_url = schema.URI(
        title=_("label_banner_url", default="Video URL"),
        description="""
        If you want the banner for this item to show a video, enter an
        external URL here.  YouTube and Vimeo are supported.  Note:
        You can either supply an image, or a video URL, not both.
        """,
        required=False,
    )

    banner_title = schema.TextLine(
        title=_("Banner Title"),
        description="",
        required=False,
    )

    banner_description = schema.Text(
        title=_("Banner Subtitle"),
        description="",
        required=False,
    )

    banner_text = RichText(
        title=_("Banner Text"),
        description="",
        required=False,
    )

    banner_link = RelationChoice(
        title=_("Banner Link"),
        description="",
        vocabulary="plone.app.vocabularies.Catalog",
        required=False,
    )

    banner_linktext = schema.TextLine(
        title=_("Link caption"),
        description=_("Caption for the link"),
        required=False,
    )

    banner_fontcolor = schema.TextLine(
        title=_("Fontcolor on the teaser"),
        description=_("Color for headings and texts as webcolor"),
        required=False,
    )

    banner_backgroundcolor = schema.TextLine(
        title=_("Background color"),
        description=_("Background color on the banner"),
        required=False,
    )


alsoProvides(IBanner, IFormFieldProvider)


@implementer(IBanner)
@adapter(IDexterityContent)
class Banner(object):
    def __init__(self, context):
        self.context = context


@indexer(IBanner)
def has_image(object, **kw):
    return (
        object.banner_image
        or object.banner_title
        or object.banner_description
        or object.banner_text
        or object.banner_link
    )
