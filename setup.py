from distutils.core import setup 

setup(
    name = 'cmsplugin_contact_plus',
    version = '1.1.3',
    packages = ['cmsplugin_contact_plus',],
    license = 'BSD License',
    url = 'https://github.com/arteria/cmsplugin-contact-plus/',
    description = 'A django CMS plugin to dynamically create contact forms.',
    long_description = open('README.md').read()+"\n",
    author = 'arteria GmbH',
    author_email = 'admin@arteria.ch',
    install_requires = ['django-inline-ordering'] #TODO: add others
)
# eof

