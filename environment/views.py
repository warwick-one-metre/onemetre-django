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

    for (id, label, type) in measurement_types:
        block['data_columns'].append(id)

        series = {}
        series['label'] = label
        series['yaxis'] = type.value
        block['series'][id] = series

    for e in queryset:
        # Truncate time to previous second
        datum = [ (e.time - reference_time).seconds ]
        for (id, label, type) in measurement_types:
            datum.append(float(getattr(e, id, 0)))

        block['data'].append(datum)

    return block

def json(request):

    class MeasurementType(Enum):
        Temperature = 1
        Humidity = 2
        Speed = 3

    INTERNAL_MEASUREMENT_TYPES = (
        ('roomalert_temp', 'Server Cupboard Temperature', MeasurementType.Temperature),
        ('roomalert_humidity', 'Server Cupboard Humidity', MeasurementType.Humidity),
        ('dome_temp', 'Internal Temperature', MeasurementType.Temperature),
        ('dome_humidity', 'Internal Humidity', MeasurementType.Humidity),
        ('underfloor_temp', 'Under Floor Temperature', MeasurementType.Temperature),
        ('underfloor_humidity', 'Under Floor Humidity', MeasurementType.Humidity),
        ('truss_temp', 'Truss Temperature', MeasurementType.Temperature),
    )

    EXTERNAL_MEASUREMENT_TYPES = (
        ('air_temperature', 'Outside Temperature', MeasurementType.Temperature),
        ('air_humidity', 'Outside Humidity', MeasurementType.Humidity),
        ('wind_speed', 'Wind Speed', MeasurementType.Speed),
    )

    reference_time = datetime.utcnow().replace(tzinfo=timezone.utc)
    internal = build_block(reference_time, INTERNAL_MEASUREMENT_TYPES, InternalEnvironmentMeasurement.objects.all())
    external = build_block(reference_time, EXTERNAL_MEASUREMENT_TYPES, ExternalEnvironmentMeasurement.objects.all())
 
    json = {}
    json['reference_time'] = int(time.mktime(reference_time.timetuple()))
    json['blocks'] = [ internal, external ]

    return JsonResponse(json)
