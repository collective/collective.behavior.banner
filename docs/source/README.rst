
collective.behavior.banner
==========================

A behavior to create banners and sliders from banners.

Features
========

The addon provides two new behaviors:

``collective.behavior.banner.banner.IBanner``
    Has various fields that can be used as a banner for one type.
    You can either add it to existing types or 'Banner'-type that only has these fields.

``collective.behavior.banner.slider.ISlider``
    Add relations several items with banners to build a slider for an existing type.
    The slider uses the js-library http://responsiveslides.com.

The banners are inherited to child-objects and you can configure which types
should display inherited banners (in the banner-controlpanel).

You can also prevent inheriting banners for an item.



How it works
============

Enable the behavior by hand or in the FTI  ``<your_package>/profiles/default/types/Folder.xml``

.. code:: xml

    <?xml version="1.0"?>
    <object name="Folder" meta_type="Dexterity FTI">
     <property name="behaviors" purge="False">
      <element value="collective.behavior.banner.banner.IBanner"/>
     </property>
    </object>



Installation
============

To install `collective.behavior.banner` you simply add ``collective.behavior.banner``
to the list of eggs in your buildout, run buildout and restart Plone.
Then, install `collective.behavior.banner` using the Add-ons control panel.


