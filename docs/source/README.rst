
collective.behavior.banner
==========================

A behavior to create banners and sliders from banners.

Features
========

Banner
------

A banner is usually some text and an image that is displayed above of the content.

The behavior ``collective.behavior.banner.banner.IBanner`` has various fields (image, title, subtitle, richtext, link, linkcaption etc) that are combined to build a banner. You can enable the behavior on any Dexterity type (tested with plone.app.contenttypes).


Slider
------

The behavior ``collective.behavior.banner.slider.ISlider`` adds th eoption to add relations to several banners (i.e. items that have the Banner-behavior enabled). These banners are then displayed like a banner but fade .

The slider-viewlet uses the js-library http://responsiveslides.com and fades from one banner to another.

Before you use a slider/carousel on your website plase take time to read this http://shouldiuseacarousel.com.


Inheriting
----------

Banners are inherited to child-objects. In a controlpanel you can configure which types should display inherited banners. You can also prevent inheriting banners for an item by enabling the option *Do not inherit banner from parents* on the banner-tab.


Customization
=============

To change the appearance (e.g. if you use a bootstrap-theme or want to use a different effect in the slider) you can easily override the respective viewlets with `z3c.jbot <http://pypi.python.org/pypi/z3c.jbot>`_ or `plone.app.themingplugins <https://pypi.python.org/pypi/plone.app.themingplugins>`_ (if you use plone.app.theming). The names of the viewlets would be ``collective.behavior.banner.browser.banner.pt`` and ``collective.behavior.banner.browser.slider.pt``.


Demo
====

collective.behavior.banner is used on the following sites:

- http://www.plone.de
- http://python-verband.org
- http://www.bildungswerk-bayern.de


Installation
============

To install `collective.behavior.banner` you simply add ``collective.behavior.banner`` to the list of eggs in your buildout, run buildout and restart Plone.
Then, install `collective.behavior.banner` using the Add-ons control panel.

Enable the behavior by hand or in the FTI  ``<your_package>/profiles/default/types/Folder.xml``

.. code:: xml

    <?xml version="1.0"?>
    <object name="Folder" meta_type="Dexterity FTI">
     <property name="behaviors" purge="False">
      <element value="collective.behavior.banner.banner.IBanner"/>
     </property>
    </object>


Contributors
============

* Philip Bauer (pbauer)
* Steffen Lindner (Gomez)
* Stefan Antonelli (santonelli)
