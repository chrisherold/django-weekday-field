from django import forms

class WeekdayWidget(forms.widgets.SelectMultiple):
    def render(self, *args, **kwargs):
        return super(WeekdayWidget, self).render(*args, **kwargs)