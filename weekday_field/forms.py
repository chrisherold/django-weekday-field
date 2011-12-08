from django import forms

import utils

class WeekdayFormField(forms.TypedMultipleChoiceField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = utils.DAY_CHOICES
        kwargs.pop('max_length', None)
        super(WeekdayFormField, self).__init__(*args, **kwargs)