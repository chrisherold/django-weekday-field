from django import forms

import functools
import operator

from weekday_field import utils, widgets

class WeekdayFormField(forms.TypedMultipleChoiceField):
    def __init__(self, *args, **kwargs):
        if 'choices' not in kwargs:
          kwargs['choices'] = utils.DAY_CHOICES
        kwargs.pop('max_length', None)
        if 'widget' not in kwargs:
          kwargs['widget'] = forms.widgets.SelectMultiple
        super(WeekdayFormField, self).__init__(*args, **kwargs)

    def clean(self, value):
        if utils.is_str(value):
            value = [int(i) for i in value.split(',')]
        value = super(WeekdayFormField, self).clean(value)
        return value

class AdvancedWeekdayFormField(WeekdayFormField):
    def __init__(self, *args, **kwargs):
        if 'choices' not in kwargs:
            kwargs['choices'] = utils.ADVANCED_DAY_CHOICES
        if 'widget' not in kwargs:
            kwargs['widget'] = widgets.ToggleCheckboxes
        super(AdvancedWeekdayFormField, self).__init__(*args, **kwargs)

    def clean(self, value):
        value = super(AdvancedWeekdayFormField, self).clean(value)
        if [int(i) for i in value] == list(range(7)):
            return []
        return value

class BitwiseWeekdayFormField(WeekdayFormField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = [(x[0],x[2]) for x in utils.BITWISE_DAY_CHOICES]
        if 'short' in kwargs:
            if kwargs['short']:
                kwargs['choices'] = [(x[0],x[1]) for x in utils.BITWISE_DAY_CHOICES]
            del kwargs['short']
        super(BitwiseWeekdayFormField, self).__init__(*args, **kwargs)

    def clean(self,value):
        value = [int(x) for x in value]
        if len(value) != 0:
            value = functools.reduce(operator.or_, value)
        else:
            value = 0
        return value
