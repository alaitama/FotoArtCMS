#!/usr/bin/env python

from setuptools import setup

setup(
    name='isaac',
    version='1.0',
    description='My personal website hosted on OpenShift.',
    author='Isaac Bythewood',
    author_email='isaac@bythewood.me',
    url='http://www.python.org/sigs/distutils-sig/',
    install_requires=['Django==1.4', 'mezzanine==1.1.4'],
)
