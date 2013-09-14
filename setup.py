from distutils.core import setup 

setup(
    name='cmsplugin_contact_plus',
    version='1.0.2',
    packages=['cmsplugin_contact_plus',],
    license='BSD License',
    url='https://github.com/arteria/cmsplugin-contact-plus/',
    description='A django CMS plugin to dynamically create contact forms.',
    long_description=open('README.md').read(),
    author='arteria GmbH',
    author_email='admin@arteria.ch',
)
# eof