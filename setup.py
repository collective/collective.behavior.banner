# -*- coding: utf-8 -*-
"""Installer for the collective.behavior.banner package."""
from setuptools import find_packages
from setuptools import setup


long_description = (
    open('README.rst').read() +
    '\n' +
    'Contributors\n' +
    '============\n' +
    '\n' +
    open('CONTRIBUTORS.rst').read() +
    '\n' +
    open('CHANGES.rst').read() +
    '\n')

setup(
    name='collective.behavior.banner',
    version='1.0b2.dev0',
    description="A behavior to create sliders with banners",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 5.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
    ],
    keywords='Python, Plone, Dexterity, behavior',
    author='Philip Bauer',
    author_email='bauer@starzel.de',
    url='http://pypi.python.org/pypi/collective.behavior.banner',
    license='BSD',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['collective', 'collective.behavior'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Plone',
        'setuptools',
        'plone.api',
    ],
    extras_require={
        'test': [
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
            'plone.app.testing',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
