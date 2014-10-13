from setuptools import setup, find_packages


setup(
    name = 'cmsplugin_contact_plus',
    version = '1.1.11', 
    packages=find_packages(),
    license = 'BSD License',
    url = 'https://github.com/arteria/cmsplugin-contact-plus/',
    description = 'A django CMS plugin to dynamically create contact forms.',
    long_description = open('README.md').read()+"\n",
    author = 'arteria GmbH',
    author_email = 'admin@arteria.ch',
    install_requires = open('requirements.txt').read().split('\n'), #TODO: add others
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
# eof
