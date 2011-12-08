from django.db import models

from forms import WeekdayFormField

class WeekdayField(models.CommaSeparatedIntegerField):

    __metaclass__ = models.SubfieldBase
    
    description = "CSV Weekday Field"
    
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 14
        super(WeekdayField, self).__init__(*args, **kwargs)
    
    def formfield(self, **kwargs):
        return super(WeekdayField, self).formfield(form_class=WeekdayFormField, **kwargs)
    
try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ['^weekday_fields\.fields\.WeekdayField'])
except ImportError:
    pass