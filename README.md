# About cmsplugin_contact_plus

[cmsplugin-contact-plus](https://github.com/arteria/cmsplugin-contact-plus/) lets you build forms for your Django CMS project
with exactly the fields you want in the order you want with a minimal effort.

Beside the regular input fields there are "auto" fields, for example to submit the referral page, or additional, hidden values.
The form will be submitted to an email address that is defined per form. This allows to cover a lot of use cases with a single and simple plugin.

cmsplugin-contact-plus is licensed under the MIT License.

## Quickstart

1. To install from [PyPI](https://pypi.python.org/pypi/cmsplugin_contact_plus/), in your virtualenv run

	```
	pip install cmsplugin_contact_plus
	```

	or to get the latest commit from GitHub,

	```
	pip install -e git+git://github.com/arteria/cmsplugin-contact-plus.git#egg=cmsplugin_contact_plus
	```


2. Put ``cmsplugin_contact_plus`` in your INSTALLED_APPS `settings.py` section and verify that the [ADMINS](https://docs.djangoproject.com/en/dev/ref/settings/#admins) setting is set as well.

3. Don't forget to migrate your database.
4. Configure Django's [e-mail settings](https://docs.djangoproject.com/en/1.8/topics/email/#quick-example) appropriately.

## Configuration/Settings

### ``CONTACT_PLUS_FROM_EMAIL``

Specify ``DEFAULT_FROM_EMAIL`` (https://docs.djangoproject.com/en/dev/ref/settings/#default-from-email) in your projects settings to send emails from a specific address. Otherwise Django's default  'webmaster@localhost' will be used.

### ``CONTACT_PLUS_REPLY_EMAIL_LABEL``

To set the reply-to header for the email automatically, specify ``CONTACT_PLUS_REPLY_EMAIL_LABEL`` in your project settings. If the label is "your email" for example, then set ``CONTACT_PLUS_REPLY_EMAIL_LABEL='your-email'`` - basically it's the slugified field label that is used to look up the reply-to email address.

### ``CONTACT_PLUS_REQUIRED_CSS_CLASS``

Defines the required CSS class, default is `required`.

### ``CMSPLUGIN_CONTACT_FORM_VALIDATORS``

Specify ``CMSPLUGIN_CONTACT_FORM_VALIDATORS`` in your projects settings to one or more [validator functions](https://docs.djangoproject.com/en/dev/ref/validators/) that are used with the CharFieldWithValidator field. Expected is a list of strings, each string should point a validator function by its full path. For example:

CMSPLUGIN_CONTACT_FORM_VALIDATORS = [
  'myproject.utils.validators.phone_number_validator',
]

### reCAPTCHA

To make the reCAPTCHA field type available to your users, add `'captcha'` to your `INSTALLED_APPS` and define your `RECAPTCHA_PUBLIC_KEY` and `RECAPTCHA_PRIVATE_KEY` as described in [django-recaptcha's README](https://github.com/praekelt/django-recaptcha/blob/develop/README.rst). A single reCAPTCHA instance per page is supported.

## Templates

If you are not using the default template settings of Django, make sure that  ``'django.template.loaders.app_directories.Loader'`` is added to the [`TEMPLATES.OPTIONS.loaders`](https://docs.djangoproject.com/en/1.8/ref/templates/upgrading/#the-templates-settings) list in your `settings.py` file. Likewise, if your Django version is < 1.8, make sure that the above-mentioned loader is in your list of [`TEMPLATE_LOADERS`](https://docs.djangoproject.com/en/1.8/ref/settings/#template-loaders).

## Features

- Dynamic form creation
- Migrations included
- Store data in the database
- Multiple languages: currently English and Spanish translations
- reCAPTCHA and simple math captcha
- django CMS 3.0 compatible
- Template support
- Track/pass hidden data
- Signals
- Multiple file and image fields for media upload
- Handle multiple forms located on the same page

## Notes

- Migrations are available with django-cms >= 3.0.6 because we depend on [this](https://github.com/divio/django-cms/blob/3.0.6/cms/migrations_django/0003_auto_20140926_2347.py) migrations file.
- Collecting data is not available if ``from.is_multipart is True`` (= the form has attached files)
- If you render a form field manually, make sure that its name is: `name="{{ field.label|slugify }}"`. This is necessary for the proper validation of the form.

## TODO and planned features .
- Widget support for each field.
- Provide examples and real life case studies
- Formatted email messages, HTML?, .as_p, ?
- Allow to re-use forms on different pages.
- Add optional Honeypot field support.
- Support more Languages
- (Your great feature here)

## Changelog
### Development

Please have a look at the latest commits for the work-in-progress development version.

### 1.3.0 - 10. 10. 2016
- Renamed plugin field `submit` to `submit_button_text` to achieve django CMS 3.3/3.4 compatibility. Please migrate your database and update your templates.

### 1.2.7 - 29. 03. 2016

- French translation
- Fix setuptools compatibility issue

### 1.2.6 - 05. 01. 2015

- Added a CharFieldWithValidator field that supports validators
- Use email subject defined in plugin settings
- Set `required_css_class` of contact form
- Use more specific setting `CONTACT_PLUS_FROM_EMAIL`, and use `DEFAULT_FROM_EMAIL` as a fallback

### 1.2.5 - 10. 11. 2015

- Handle multiple forms located on the same page. See the two relevant commits [7749d44](https://github.com/arteria/cmsplugin-contact-plus/commit/7749d44d39f1b106a1b4c980615fab7a6a810a37) and [b8793f7](https://github.com/arteria/cmsplugin-contact-plus/commit/b8793f7bc0ce573bbed1bb9ffa20f9b87191fa8b) for more info. Please modify your templates.

### 1.2.3

- reCAPTCHA support

### 1.1.14 - 20. 03. 2015

- Multiple file and image fields / Upload files and images, upload will be placed directly into ``MEDIA_ROOT``.

### 1.1.13 - 17. 11. 2014

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

- django CMS 3.0 caching compatibility.

### 1.1.6

- Bugfix, missing template info, https://github.com/arteria/cmsplugin-contact-plus/commit/1fa9236

### 1.1.5

- Trigger a signal ``contact_message_sent`` when a message was sent successfully. See signals.py .
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
- Improved Documentation
- Added ``auto_TextArea`` shortcut to create a TextArea. Note: Currently the widget defined in the plugins are ignored.
- Hidden "referral page" field. Reads referral from request.
- Generic Hidden fields. Use this in combination with JavaScript/jQuery to attach additional data to the form sent by email.

For example, the field lable for the 'CharField as HiddenInput' is named to "Object description".
Using the lable name, the ID for the input field will be 'id_object-description', the name 'object-description'.

Store data is dead easy using jQuery.


	$('#id_object-description').val('Hello Hidden World'); // The string 'Hello Hidden World' will be send by email as well.



### 1.0.2
Fixed indentation /EOF in setup.py


### 1.0.1
Fixed IndentationError in setup.py

### 1.0.0
[arteria](https://github.com/arteria/) open sourced cmsplugin_contact_plus unter the MIT License. This plugin was built on a fork of [cmsplugin_contact](https://github.com/rtpm/cmsplugin_contact). Kudos!
