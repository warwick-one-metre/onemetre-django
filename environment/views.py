from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime, timezone
from enum import Enum
import time
from .models import ExternalEnvironmentMeasurement, InternalEnvironmentMeasurement

# Create your views here.

def index(request):
	context = {}
	return render(request, 'environment/environment.html', context)

def build_block(reference_time, measurement_types, queryset):
    block = {}
    block['series'] = {}
    block['data_columns'] = [ 'time' ]
    block['data'] = []

    for (id, label) in measurement_types:
        block['data_columns'].append(id)

        series = {}
        series['label'] = label
        block['series'][id] = series

    for e in queryset:
        # Truncate time to previous second
        datum = [ int((e.time - reference_time).total_seconds()) ]
        for (id, label) in measurement_types:
            datum.append(float(getattr(e, id, 0)))

        block['data'].append(datum)

    return block

def json_temperature(request):

    INTERNAL_MEASUREMENT_TYPES = (
        ('roomalert_temp', 'Server Cupboard'),
        ('dome_temp', 'Dome'),
        ('underfloor_temp', 'Under Floor'),
        ('truss_temp', 'Truss'),
    )

    EXTERNAL_MEASUREMENT_TYPES = (
        ('air_temperature', 'Outside'),
    )

    reference_time = datetime.utcnow().replace(tzinfo=timezone.utc)
    internal = build_block(reference_time, INTERNAL_MEASUREMENT_TYPES, InternalEnvironmentMeasurement.objects.all())
    external = build_block(reference_time, EXTERNAL_MEASUREMENT_TYPES, ExternalEnvironmentMeasurement.objects.all())
 
    json = {}
    json['reference_time'] = int(time.mktime(reference_time.timetuple()))
    json['blocks'] = [ internal, external ]
    json['axis_label'] = 'Temperature (&deg;C)'

    return JsonResponse(json)


def json_humidity(request):

    INTERNAL_MEASUREMENT_TYPES = (
        ('roomalert_humidity', 'Server Cupboard'),
        ('dome_humidity', 'Dome'),
        ('underfloor_humidity', 'Under Floor'),
    )

    EXTERNAL_MEASUREMENT_TYPES = (
        ('air_humidity', 'Outside'),
    )

    reference_time = datetime.utcnow().replace(tzinfo=timezone.utc)
    internal = build_block(reference_time, INTERNAL_MEASUREMENT_TYPES, InternalEnvironmentMeasurement.objects.all())
    external = build_block(reference_time, EXTERNAL_MEASUREMENT_TYPES, ExternalEnvironmentMeasurement.objects.all())
 
    json = {}
    json['reference_time'] = int(time.mktime(reference_time.timetuple()))
    json['blocks'] = [ internal, external ]
    json['axis_label'] = 'Relative Humidity (%)'
    return JsonResponse(json)
