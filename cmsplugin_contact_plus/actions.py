import csv 
from six import text_type

from django.http import HttpResponse


class LUT(object):
        
    def __init__(self):
        self.lut = []
            
    def add_field(self, field_name):
        """ """
        if field_name not in self.lut:
            self.lut.append(field_name)
            
    def get_idx(self, field_name):
        """ """
        return self.lut.index(field_name)
    
    
    
def export_as_csv_action(description="Export selected objects as CSV file",
                         fields=None, exclude=None, header=True, json_fields=None):
    """
    This function returns an export csv action
    'fields' and 'exclude' work like in django ModelForm
    'header' is whether or not to output the column names as the first row
    
    json_fields will be exploaded to rows.
    """

    from itertools import chain

    def export_as_csv(modeladmin, request, queryset):
        """
        Generic csv export admin action.
        based on http://djangosnippets.org/snippets/2369/
        """
        opts = modeladmin.model._meta
        field_names = set([field.name for field in opts.fields])
        many_to_many_field_names = set([many_to_many_field.name for many_to_many_field in opts.many_to_many])
        if fields:
            fieldset = set(fields)
            field_names = field_names & fieldset
        elif exclude:
            excludeset = set(exclude)
            field_names = field_names - excludeset

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=%s.csv' % text_type(opts).replace('.', '_')
        
        writer = csv.writer(response)
        """
        if header:
            writer.writerow(list(chain(field_names, many_to_many_field_names)))
        # default: does not split json_fields to rows. (json is in one row) 
        if not json_fields:
            for obj in queryset:
                row = []
                for field in field_names:
                    row.append(text_type(getattr(obj, field)))
                for field in many_to_many_field_names:
                    row.append(text_type(getattr(obj, field).all()))
                writer.writerow(row)
        else:
        """
        # build LUT
        lut = LUT()
        for obj in queryset:
            for field in field_names:
                if field in json_fields:
                    j = getattr(obj, field)
                    for l in j:
                        try:
                            for k, v in l.iteritems(): 
                                lut.add_field(k)
                        except AttributeError:
                            pass
                else:
                    lut.add_field(field)
        
        if header:
            writer.writerow(lut.lut)
        for obj in queryset:
            row = ['']*len(lut.lut)
            for field in field_names:
                if field in json_fields:
                    j = getattr(obj, field)
                    for l in j:
                        for k, v in l.iteritems(): 
                            try:
                                row[lut.get_idx(k)] = v.encode('utf-8')
                            except AttributeError:
                                pass
                else:
                    row[lut.get_idx(field)] = text_type(getattr(obj, field))
            for field in many_to_many_field_names:
                row[lut.get_idx(field)] = text_type(getattr(obj, field).all())
            writer.writerow(row)
            
            
        return response
    export_as_csv.short_description = description
    return export_as_csv