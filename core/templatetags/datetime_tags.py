import datetime
import pytz
from django.conf import settings
from django import template

register = template.Library()


@register.simple_tag
def time_of_day():
    cur_time = datetime.datetime.now(
        tz=pytz.timezone(str(settings.TIME_ZONE)))
    print(cur_time.hour)
    if cur_time.hour < 12:
        return 'Morning'
    elif 12 <= cur_time.hour < 18:
        return 'Afternoon'
    else:
        return 'Evening'
