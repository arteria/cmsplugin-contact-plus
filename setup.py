import os
import sys
import cmsplugin_contact_plus

from distutils.core import setup
from setuptools import setup, find_packages

version = cmsplugin_contact_plus.__version__

setup(
    name = 'cmsplugin_contact_plus',
    version = version, 
    packages=find_packages(),
    license = 'BSD',
    url = 'https://github.com/arteria/cmsplugin-contact-plus/',
    description = 'A django CMS plugin to dynamically create contact forms.',
    long_description = open('README.md').read()+"\n",
    author = 'arteria GmbH',
    author_email = 'admin@arteria.ch',
    install_requires=open('requirements.txt').read().split('\n'), #TODO: add others
    include_package_data=True
)
# eof
