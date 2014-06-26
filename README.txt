=====================
django-weekday-field
=====================

 |status|

A field that encapsulates the handling of selection of 0 or more weekday choices.

Uses Django's CommaSeparatedIntegerField internally.

Usage:

    from django.db import models

    import weekday_field

    class MyModel(models.Model):
        weekdays = weekday_field.fields.WeekdayField()


There is also a BitwiseWeekdayFormField, contributed by Andrew Gall <housepage@gmail.com>, which stores the data in a single integer.

Thanks to NaderM <https://bitbucket.org/NaderM>, 1.1.0 includes python3 support, and extensive testing.

.. |status| image:: https://drone.io/bitbucket.org/schinckel/django-weekday-field/status.png
