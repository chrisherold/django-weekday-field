from django import forms

import utils
import operator

class WeekdayFormField(forms.TypedMultipleChoiceField):
    def __init__(self, *args, **kwargs):
        if 'choices' not in kwargs:
          kwargs['choices'] = utils.DAY_CHOICES
        kwargs.pop('max_length', None)
        if 'widget' not in kwargs:
          kwargs['widget'] = forms.widgets.SelectMultiple
        super(WeekdayFormField, self).__init__(*args, **kwargs)
        
    def clean(self, value):
      value = super(WeekdayFormField, self).clean(value)
      return value

class BitwiseWeekdayFormField(WeekdayFormField):
  def __init__(self, *args, **kwargs):
    if 'short' in kwargs:
      if kwargs['short']:
        kwargs['choices'] = [(x[0],x[1]) for x in utils.BITWISE_DAY_CHOICES]
      del kwargs['short']
    else:
      kwargs['choices'] = [(x[0],x[2]) for x in utils.BITWISE_DAY_CHOICES]
    super(BitwiseWeekdayFormField, self).__init__(*args, **kwargs)

  def clean(self,value):
    value = [int(x) for x in value]
    if len(value) != 0:
      value = reduce(operator.or_, value)
    else:
      value = 0
    return value
