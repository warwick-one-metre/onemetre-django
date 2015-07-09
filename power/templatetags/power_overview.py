from django import template
from power.models import PowerMeasurement

register = template.Library()

@register.inclusion_tag('power/power_overview.html')
def show_power():
    latest_power = PowerMeasurement.objects.latest()
    return {'latest_power': latest_power}
