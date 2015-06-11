from django import template
from environment.models import ExternalEnvironmentMeasurement, InternalEnvironmentMeasurement

register = template.Library()

@register.inclusion_tag('environment/external_overview.html')
def show_external_environment():
    latest_internal = ExternalEnvironmentMeasurement.objects.latest()
    return {'latest_internal': latest_internal}

# TODO: Hook up real data
@register.inclusion_tag('environment/internal_overview.html')
def show_internal_environment():
    return {}

# TODO: Hook up real data
@register.inclusion_tag('environment/power_overview.html')
def show_power():
    return {}

# TODO: Hook up real data
@register.inclusion_tag('environment/telescope_overview.html')
def show_telescope():
    return {}