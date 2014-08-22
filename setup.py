# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

with open('docs/requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='tango-admin',
    version='0.2',
    author=u'Tim Baxter',
    author_email='mail.baxter@gmail.com',
    url='http://github.com/tBaxter/tango-admin',
    license='LICENSE.txt',
    description='Simple admin helpers for Tango apps',
    long_description=open('README.md').read(),
    packages=find_packages(),
    install_requires=required,
    zip_safe=False,
    include_package_data=True,
)
