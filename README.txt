It's a extende contact form application for multi-lang sites.
This is a fork of https://bitbucket.org/arteria/cmsplugin_contact

Put "cmsplugin_contact_plus.contact" in your INSTALLED_APPS settings.py section.
Don't forget to syncdb your database.

TODO:
- save send data to DB
- signals: message send, allow further interaction
- message status for further interactions (new, in progress, closed)
- display success message or redirect to a CMS page (if cms page is set)


label: "a text label" as string
input-type: select, text, number, ... 
	select:	TagA:ValueA:seleted|TagB:ValueB
mandatory true/false
min,max, placeholders and all other html5 features

start

type: select or email|number|text|url see http://www.w3schools.com/html/html5_form_input_types.asp for more
default
placeholder
mandatory (bool)
validate (bool)


end