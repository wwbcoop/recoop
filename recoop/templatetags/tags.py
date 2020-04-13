# django
from django import template
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
# project
from django.conf import settings

register = template.Library()

@register.filter(name='remove_i18n_prefix')
def remove_i18n_prefix(value):
    if value.startswith('/en') or value.startswith('/es'):
        value = value[3::]
    return value
