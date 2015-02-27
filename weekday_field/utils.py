from django.utils.translation import ugettext_lazy as _

DAY_CHOICES = (
    (0, _("Monday")),
    (1, _("Tuesday")),
    (2, _("Wednesday")),
    (3, _("Thursday")),
    (4, _("Friday")),
    (5, _("Saturday")),
    (6, _("Sunday"))
)

BITWISE_DAY_CHOICES = (
    (1, "Su",_("Sunday")),
    (2, "M",_("Monday")),
    (4, "Tu",_("Tuesday")),
    (8, "W",_("Wednesday")),
    (16, "Th",_("Thursday")),
    (32, "F",_("Friday")),
    (64, "Sa",_("Saturday")),
)

ADVANCED_DAY_CHOICES = (
    ("0,1,2,3,4,5,6", _("Any day")),
    ("0,1,2,3,4", _("Weekdays")),
    ("5,6", _("Weekends")),
) + DAY_CHOICES

def is_str(obj):
    try:
        return isinstance(obj, basestring)
    except NameError:
        return isinstance(obj, str)
