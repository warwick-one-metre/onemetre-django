from django import template
from django.utils.safestring import mark_safe
from power.models import PowerMeasurement

register = template.Library()

@register.filter()
def onoff(value):
    if (value):
        return mark_safe('<span style="color: #090">ON</span>')

    return mark_safe('<span style="color: #C00">OFF</span>')

@register.filter()
def powerbattery(value):
    if (value):
        return mark_safe('<span style="color: #090">POWERED</span>')

    return mark_safe('<span style="color: #C00">BATTERY</span>')

@register.filter()
def ups_status(value):

    color = '#090' if value == 'Online' else '#C00';
    return mark_safe('<span style="color: '+color+'">'+value.upper()+'</span>')

@register.filter()
def battery_percentage(value):
    percent = int(value)
    color = '#090' if percent > 66 else '#FA0' if percent > 33 else '#C00';
    return mark_safe('<span style="color: '+color+'">'+value+'%</span>')

@register.filter()
def load_percentage(value):
    percent = int(value)
    color = '#C00' if percent > 66 else '#FA0' if percent > 33 else '#090';
    return mark_safe('<span style="color: '+color+'">'+value+'%</span>')


