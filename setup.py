#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import join, dirname
from setuptools import setup, find_packages
import cmsplugin_contact_plus as app


def long_description():
    try:
        return open(join(dirname(__file__), 'README.rst')).read()
    except IOError:
        return "LONG_DESCRIPTION Error"


setup(
    name='cmsplugin_contact_plus',
    version=app.__version__,
    packages=find_packages(),
    license='BSD License',
    url='https://github.com/arteria/cmsplugin-contact-plus/',
    description='A django CMS plugin to dynamically create contact forms.',
    long_description=long_description(),
    author='arteria GmbH',
    author_email='admin@arteria.ch',
    # TODO: add others
    install_requires=open('requirements.txt').read().split('\n'),
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Framework :: Django',
    ],
)
