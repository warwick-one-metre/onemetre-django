from django import template
from environment.models import ExternalEnvironmentMeasurement, SQTRoomAlertMeasurement

register = template.Library()

@register.inclusion_tag('environment/external_overview.html')
def show_external_environment():
    latest_external = ExternalEnvironmentMeasurement.objects.latest()
    return {'latest_external': latest_external}

# TODO: Hook up real data
@register.inclusion_tag('environment/internal_overview.html')
def show_internal_environment():
    return {}

# TODO: Hook up real data
@register.inclusion_tag('environment/telescope_overview.html')
def show_telescope():
    return {}
