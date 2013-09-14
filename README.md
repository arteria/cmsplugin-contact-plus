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

2. Put "cmsplugin_contact_plus" in your INSTALLED_APPS settings.py section and verify that [ADMINS](https://docs.djangoproject.com/en/dev/ref/settings/#admins) is defined as well.

3. Don't forget to syncdb your database.

## Templates

Do not forget to add `'django.template.loaders.app_directories.Loader'` to `TEMPLATE_DIRS` in your settings.py.   


## TODO
- Save send data to a NoSQL database (eg. MongoDB).
- Trigger a signal when a message was send successfully
- and track the current status in each message record for further interaction (new, in progress, closed). 
- Add dependencies to setup.py.



## Changelog
### development
- Documentation

### 1.0.2
Fixed indentation /EOF in setup.py


### 1.0.1
Fixed IndentationError in setup.py

### 1.0.0

[arteria](https://github.com/arteria/) open sourced cmsplugin_contact_plus.



