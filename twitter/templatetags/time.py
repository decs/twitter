from django import template
from django.utils.dateformat import format
import datetime

register = template.Library()

@register.filter
def relativo(value, autoescape=None):
    diff = datetime.datetime.now() - value
    s = diff.seconds
    if diff.days > 7 or diff.days < 0:
        return format(value, 'd b y')
    elif diff.days == 1:
        return 'há 1 dia'
    elif diff.days > 1:
        return 'há {} dias'.format(diff.days)
    elif s <= 1:
        return 'agora'
    elif s < 60:
        return 'há {} segundos'.format(s)
    elif s < 120:
        return 'há 1 minuto'
    elif s < 3600:
        return 'há {} minutos'.format(s/60)
    elif s < 7200:
        return 'há 1 hora'
    else:
        return 'há {} horas'.format(s/3600)
relativo.needs_autoescape = True
