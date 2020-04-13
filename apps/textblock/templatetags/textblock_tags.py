# django
from django import template
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
# project
from django.conf import settings
from apps.textblock.models import TextBlock

register = template.Library()

@register.simple_tag
def textblock(title, lang):
    block = TextBlock.objects.filter(title__iexact=title).first()
    default_lang = settings.LANGUAGE_CODE
    body = 'body'
    if lang != default_lang:
        body += '_%s' % lang
    if block:
        return mark_safe( getattr(block, body) )
    return ''
