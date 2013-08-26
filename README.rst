# cmsplugin_contact_plus


[cmsplugin_contact_plus](https://github.com/arteria/cmsplugin-contact-plus/) is an adapted version of [cmsplugin_contact](https://github.com/rtpm/cmsplugin_contact).


## Quickstart

1. In your virtualenv run

	```
	pip install cmsplugin_contact_plus
	```

2. Put "cmsplugin_contact_plus.contact" in your INSTALLED_APPS settings.py section and verify that [ADMINS](https://docs.djangoproject.com/en/dev/ref/settings/#admins) is defined as well.

3. Don't forget to syncdb your database.




## TODO
- Save send data to a NoSQL database (eg. MongoDB).
- Trigger a signal when a message was send successfully
- and track the current status in each message record for further interaction (new, in progress, closed). 

https://github.com/maccesch/cmsplugin-contact


## Changelog


### 1.0.0

Open sourced cmsplugin_contact_plus.



