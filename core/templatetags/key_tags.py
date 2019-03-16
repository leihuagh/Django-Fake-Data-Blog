from django.conf import settings
from django import template

register = template.Library()


@register.simple_tag(name='get_google_map_api_key')
def get_google_map_api_key():
    return settings.GOOGLE_MAP_API_KEY
