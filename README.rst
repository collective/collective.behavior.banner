
collective.behavior.teaser
==========================

A behavior to create teasers and sliders from teasers

* `Source code @ GitHub <https://github.com/starzel/collective.behavior.teaser>`_
* `Releases @ PyPI <http://pypi.python.org/pypi/collective.behavior.teaser>`_
* `Documentation @ ReadTheDocs <http://collectivebehaviorteaser.readthedocs.org>`_
* `Continuous Integration @ Travis-CI <http://travis-ci.org/collective/collective.behavior.teaser>`_

How it works
============

Enable the behavior in ``<your_package>/profiles/default/types/Folder.xml``

.. code:: xml

    <?xml version="1.0"?>
    <object name="Folder" meta_type="Dexterity FTI">
     <property name="behaviors" purge="False">
      <element value="collective.behavior.teaser.teaser.ITeaser"/>
     </property>
    </object>



Installation
============

To install `collective.behavior.teaser` you simply add ``collective.behavior.teaser``
to the list of eggs in your buildout, run buildout and restart Plone.
Then, install `collective.behavior.teaser` using the Add-ons control panel.


Configuration
=============

...

