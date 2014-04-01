
collective.behavior.banner
==========================

A behavior to create banners and sliders from banners

* `Source code @ GitHub <https://github.com/starzel/collective.behavior.banner>`_
* `Continuous Integration <https://jenkins.starzel.de/job/collective.behavior.banner>`_

How it works
============

Enable the behavior in ``<your_package>/profiles/default/types/Folder.xml``

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


Configuration
=============

...

