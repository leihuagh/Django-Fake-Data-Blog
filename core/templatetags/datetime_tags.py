
from django.conf import settings
from django import template
import datetime

register = template.Library()


@register.simple_tag
def time_of_day():
    hour = datetime.datetime.now().hour
    if hour < 12:
        return 'Morning'
    elif 12 <= hour < 18:
        return 'Afternoon'
    else:
        return 'Evening'