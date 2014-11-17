# About cmsplugin_contact_plus

[cmsplugin_contact_plus](https://github.com/arteria/cmsplugin-contact-plus/) lets your build forms for your django CMS project 
with exactly the fields you want in the order you want with a minimal effort. 

Beside the regular input fields, there are "auto" fields, for example to submit the referral page or additional, hidden values. 
The form will be submitted to a per form defined email address. This allows to cover a lot of 
use cases with a single and simple cmsplugin. 

cmsplugin_contact_plus is licensed under The MIT License.

## Quickstart

1. To install from [PyPI](https://pypi.python.org/pypi/cmsplugin_contact_plus/), in your virtualenv run

	```
	pip install cmsplugin_contact_plus
	```
	
	or to get the latest commit from GitHub
	 
	```
	pip install -e git+git://github.com/arteria/cmsplugin-contact-plus.git#egg=cmsplugin_contact_plus
	```
	

2. Put ``cmsplugin_contact_plus`` in your INSTALLED_APPS settings.py section and verify that [ADMINS](https://docs.djangoproject.com/en/dev/ref/settings/#admins) is defined as well.

3. Don't forget to syncdb your database.

## Configuration/Settings

### ``DEFAULT_FROM_EMAIL``

Specify ``DEFAULT_FROM_EMAIL`` (https://docs.djangoproject.com/en/dev/ref/settings/#default-from-email) in your projects settings to send emails from a specific address. Otherwise Django's default  'webmaster@localhost' will be used. 

### ``CONTACT_PLUS_REPLY_EMAIL_LABEL``

To set the reply-to header for the email automatically, specify ``CONTACT_PLUS_REPLY_EMAIL_LABEL`` in your project settings. If the label is "your email" for example, then set ``CONTACT_PLUS_REPLY_EMAIL_LABEL='your-email'`` - basically it's the slugified field label that is used to lookup the reply-to email address.

## Templates

Do not forget to add ``'django.template.loaders.app_directories.Loader'`` to ``TEMPLATE_LOADERS`` in your settings.py.

## Notes
- Mirgations are available with django-cms >= 3.0.6, cause we depend on [this](https://github.com/divio/django-cms/blob/3.0.6/cms/migrations_django/0003_auto_20140926_2347.py) migrations file.

## TODO and planned features
- Add/Update dependencies to setup.py.
- Widget support for each field.
- Provide examples and real life case studies
- Formatted email messages, HTML?, .as_p, ? 
- Allow to reuse forms on different pages.
- Add optional Honeypot field support.
- Support more Languages

## Done
- Migrations
- Save sent data in the database.

## Changelog
### Development 
Please have a look at the latest commits for the work-in-progress-development version.

- .

### 1.1.13 - 17.11.2014

- Adding Spanish translation
- Support migrations for django __1.7__ and django cms __3.0.6__

### 1.1.12

- Reply-to email support
- Added ContactRecords to store Contact History in the Database.

### 1.1.11

- Integration of a simple math captcha (PR #16)

### 1.1.10

- Removed unordered data (cleaned_data). Now use ordered_data instead.
- Fixed typo

### 1.1.9

- Fixed lower() vs. slugify() for key lookup.

### 1.1.8

- Field ordering in the email is now equal to the definition.

### 1.1.7

- django-cms 3.0 caching compatibility.

### 1.1.6

- Bugfix, missing template info, https://github.com/arteria/cmsplugin-contact-plus/commit/1fa9236

### 1.1.5

- Trigger a signal ``contact_message_sent`` when a message was send successfully. See signals.py .
- Multiple templates support, in your project settings define

	```
	CMSPLUGIN_CONTACT_PLUS_TEMPLATES = [
		('cmsplugin_contact_plus/contact.html', 'contact.html'),
        ('cmsplugin_contact_plus/hello.html', 'hello.html'),
		# more templates here
    ]
	```
	
	To be able to use the new features, please migrate manually
	
	``` ALTER TABLE `cmsplugin_contactplus` ADD `template` varchar(255) NOT NULL AFTER  `submit`; ```

### 1.1.4

- Packaging was modified for PyPI.
- Upload script for PyPI. Internal note: just execute ``./upload-to-pypi.sh``.


### 1.1.3
- Better readability in email.

### 1.1.2
- Patch version for PyPI with corrected Manifest.in, see issue #4.

### 1.1.1
- Added include for templates im Manifest.in, fixes issue #4.

### 1.1.0
- Generic Query parameter (GET key) to hidden field. Use this in attach additional hidden data to the form. The slugified label is used for key lookup in the GET parameters. Eg.:
label is 'Favorite Color', than the lookup in the URL is done based on 'favorite-color', in www.example.com?favorite-color=blue will pass {..., u'favorite-color':'blue', ...}  to the email.


### 1.0.4
- Fixed default "from email address" in case ``ADMINS`` is not defined in ``settings.py``. (Issue #2)
- Fixed typos and added translation markers.

### 1.0.3
- Improoved Documentation
- Added ``auto_TextArea`` shortcut to create a TextArea. Note: Currently the widget definde in the plugins are ignored. 
- Hidden "referral page" field. Reads referral from request.
- Generic Hidden fields. Use this in combination with JavaScript/jQuery to attach additional data to the form sent by email.

For exmple, the field lable for the 'CharField as HiddenInput' is named to "Object description". 
Using the lable name, the ID for the input field will be 'id_object-description', the name 'object-description'.

Store data is dead easy using jQuery.

	
	$('#id_object-description').val('Hello Hidden World'); // The string 'Hello Hidden World' will be send by email as well.
	


### 1.0.2
Fixed indentation /EOF in setup.py


### 1.0.1
Fixed IndentationError in setup.py

### 1.0.0
[arteria](https://github.com/arteria/) open sourced cmsplugin_contact_plus unter the MIT License. This plugin was build on a fork of [cmsplugin_contact](https://github.com/rtpm/cmsplugin_contact). Kudos! 
