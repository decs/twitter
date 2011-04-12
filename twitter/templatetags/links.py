from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
import re

register = template.Library()

@register.filter
def usuarios(value, autoescape=None):
    value = conditional_escape(value)
    user = re.compile('(\s|^)(@)(\w+)(\s|$)')
    value = user.sub('\\1<a href="/\\3">\\2\\3</a>\\4', value)
    return mark_safe(value)
usuarios.needs_autoescape = True

@register.filter
def hashtags(value, autoescape=None):
    value = conditional_escape(value)
    hashtag = re.compile('(\s|^)(#)(\w+)(\s|$)')
    value = hashtag.sub('\\1<a href="/buscar/?termo=%23\\3">\\2\\3</a>\\4', value)
    return mark_safe(value)
hashtags.needs_autoescape = True