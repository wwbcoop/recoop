# python
import os.path
# django
from django import template
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
# project
from django.conf import settings

register = template.Library()

# Shortcut to css assets in the main static folder
@register.simple_tag
def css(file):
    return  settings.STATIC_URL + settings.PROJECT_STATIC_FOLDER + '/css/' + file

# Shortcut to js assets in the main static folder
@register.simple_tag
def js(file):
    return  settings.STATIC_URL + settings.PROJECT_STATIC_FOLDER + '/js/' + file

# Shortcut to img assets in the main static folder
@register.simple_tag
def img(file):
    return  settings.STATIC_URL + settings.PROJECT_STATIC_FOLDER + '/img/' + file

# A simple JS breadcrumb
@register.inclusion_tag('fake-breadcrumb.html')
def fake_breadcrumb(text=_("Volver a la página anterior")):
    return { 'text' : text }

# Generates a range to iterate over
@register.filter
def get_range(max):
    return range(max)

# Filter to concatenate two strings
@register.filter
def addstr(arg1, arg2):
    """concatenate arg1 & arg2"""
    return str(arg1) + str(arg2)
