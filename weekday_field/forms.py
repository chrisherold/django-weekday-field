from django import forms

import utils

class WeekdayFormField(forms.TypedMultipleChoiceField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = utils.DAY_CHOICES
        kwargs.pop('max_length', None)
        kwargs['widget'] = forms.widgets.SelectMultiple
        super(WeekdayFormField, self).__init__(*args, **kwargs)
        
    def clean(self, value):
        value = super(WeekdayFormField, self).clean(value)
        return ",".join([str(x) for x in value])