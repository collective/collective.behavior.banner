collective.behavior.banner
==========================

A behavior to create banners and sliders from banners.

Features
========

Banner
------

A banner is usually some text and an image that is displayed above of the content.

The behavior ``collective.behavior.banner.banner.IBanner`` has various fields (image, title, subtitle, richtext, link, linkcaption etc) that are combined to build a banner. You can enable the behavior on any Dexterity type (tested with plone.app.contenttypes) or for the whole Plone site.


Slider
------

The behavior ``collective.behavior.banner.slider.ISlider`` adds the option to add relations to several banners (i.e. items that have the Banner behavior enabled). These banners are then displayed like a banner but fade.

The slider viewlet uses the javascript library http://responsiveslides.com and fades from one banner to another. You can easily use a different javascript libray by overriding the viewlet templates (see below).

Before you use a slider/carousel on your website, please take time to read http://shouldiuseacarousel.com.


Inheriting
----------

Banners are inherited by child objects. In a controlpanel you can configure which types should display inherited banners. You can also prevent inheriting banners for an item and its child objects by enabling the option *Do not inherit banner from parents* on the banner tab. If you want a banner for the entire site, you can assign one to the default content of the Navigation Root (or Plone site root).


Customization
=============

To change the appearance (e.g. if you use a bootstrap theme or want to use a different effect in the slider) you can easily override the respective viewlets with `z3c.jbot <http://pypi.python.org/pypi/z3c.jbot>`_ or `plone.app.themingplugins <https://pypi.python.org/pypi/plone.app.themingplugins>`_ (if you use plone.app.theming). The names of the files to create would be ``collective.behavior.banner.browser.banner.pt`` and ``collective.behavior.banner.browser.slider.pt``.


Demo
====

collective.behavior.banner is used on the following sites:

* http://www.plone.de
* http://python-verband.org
* http://www.bildungswerk-bayern.de


Compatibility
=============

collective.behavior.banner works in Plone 4, 5 and 6.

* Plone 6: 2.x
* Plone 5: 1.x
* Plone 4: 0.x


Installation
============

To install `collective.behavior.banner` you simply add ``collective.behavior.banner`` to the list of eggs in your buildout, run buildout and restart Plone. Then, install `collective.behavior.banner` using the Add-ons control panel.

Enable the behavior by hand or in the FTI  ``<your_package>/profiles/default/types/Folder.xml``:

.. code:: xml

    <?xml version="1.0"?>
    <object name="Folder" meta_type="Dexterity FTI">
     <property name="behaviors" purge="False">
      <element value="collective.behavior.banner.banner.IBanner"/>
     </property>
    </object>


Contribute
----------

* Source Code: https://github.com/collective/collective.behavior.banner
* Issue Tracker: https://github.com/collective/collective.behavior.banner/issues


Support
-------

If you are having issues, please let us know at https://github.com/collective/collective.behavior.banner/issues.

