from django import template
from django.utils.safestring import mark_safe
from power.models import PowerMeasurement

register = template.Library()

@register.filter()
def openclose(value):
    if (value):
        return mark_safe('<span style="color: #090">OPEN</span>')

    return mark_safe('<span style="color: #C00">CLOSED</span>')

@register.filter()
def opencloseinverted(value):
    return openclose(not value)

@register.filter()
def onoff(value):
    if (value):
        return mark_safe('<span style="color: #090">ON</span>')

    return mark_safe('<span style="color: #C00">OFF</span>')

