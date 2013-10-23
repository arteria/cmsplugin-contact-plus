# cmsplugin_contact_plus


[cmsplugin_contact_plus](https://github.com/arteria/cmsplugin-contact-plus/) is an adapted version of [cmsplugin_contact](https://github.com/rtpm/cmsplugin_contact).


## Quickstart

1. To install from PyPi, in your virtualenv run

	```
	$ pip install cmsplugin_contact_plus
	```
	
	or to get the latest commit from GitHub
	 
	```
	$ pip install -e git+git://github.com/arteria/cmsplugin-contact-plus.git#egg=cmsplugin_contact_plus
	```
	

2. Put ``cmsplugin_contact_plus`` in your INSTALLED_APPS settings.py section and verify that [ADMINS](https://docs.djangoproject.com/en/dev/ref/settings/#admins) is defined as well.

3. Don't forget to syncdb your database.

## Templates

Do not forget to add ``'django.template.loaders.app_directories.Loader'`` to ``TEMPLATE_DIRS`` in your settings.py.   


## TODO
- Save send data to a NoSQL database (eg. MongoDB).
- Trigger a signal when a message was send successfully
- and track the current status in each message record for further interaction (new, in progress, closed). 
- Add dependencies to setup.py.
- Widget support for each field.  
- Smart hidden fields, eg. storing Query parameter, ..


## Changelog
### development

### 1.0.3
- Improoved Documentation
- Added ``auto_TextArea`` shortcut to create a TextArea. Note: Currently the widget definde in the plugins are ignored. 
- Hidden "referral page" field. Reads referral from request.
- Generic Hidden fields. Use this in combination with JavaScript/jQuery to attach additional data to the form sent by email.

For exmple, the field lable for the 'CharField as HiddenInput' is named to "Object description". 
Using the lable name, the ID for the input field will be 'id_object-description', the name 'object-description'.

Store data is dead easy using jQuery.

	```
	$('#id_object-description').val('Hello Hidden World'); // The string 'Hello Hidden World' will be send by email as well.
	```


### 1.0.2
Fixed indentation /EOF in setup.py


### 1.0.1
Fixed IndentationError in setup.py

### 1.0.0

[arteria](https://github.com/arteria/) open sourced cmsplugin_contact_plus.



