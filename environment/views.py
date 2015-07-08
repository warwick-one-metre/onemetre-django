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

def json(request):

    class MeasurementType(Enum):
        Temperature = 1
        Humidity = 2
        Speed = 3

    MEASUREMENT_TYPES = (
        # Internal Measurements
        ('roomalert_temp', 'Server Cupboard Temperature', MeasurementType.Temperature),
        ('roomalert_humidity', 'Server Cupboard Humidity', MeasurementType.Humidity),
        ('dome_temp', 'Internal Temperature', MeasurementType.Temperature),
        ('dome_humidity', 'Internal Humidity', MeasurementType.Humidity),
        ('underfloor_temp', 'Under Floor Temperature', MeasurementType.Temperature),
        ('underfloor_humidity', 'Under Floor Humidity', MeasurementType.Humidity),
        ('truss_temp', 'Truss Temperature', MeasurementType.Temperature),

        # External Measurements
        ('air_temperature', 'Outside Temperature', MeasurementType.Temperature),
        ('air_humidity', 'Outside Humidity', MeasurementType.Humidity),
        ('wind_speed', 'Wind Speed', MeasurementType.Speed),
    )

    json = []

    data_arrays = {}
    for (id, label, type) in MEASUREMENT_TYPES:
        data = []
        data_arrays[id] = data

        measurement = {}
        measurement['label'] = label
        measurement['data'] = data
        measurement['yaxis'] = type.value
        json.append(measurement)

    for e in ExternalEnvironmentMeasurement.objects.all():
        ms = time.mktime(e.time.timetuple()) * 1000
        data_arrays['air_temperature'].append([ms, float(e.air_temperature)])
        data_arrays['air_humidity'].append([ms, float(e.air_humidity)])
        data_arrays['wind_speed'].append([ms, float(e.wind_speed)])

    for e in InternalEnvironmentMeasurement.objects.all():
        ms = time.mktime(e.time.timetuple()) * 1000
        data_arrays['roomalert_temp'].append([ms, float(e.roomalert_temp)])
        data_arrays['roomalert_humidity'].append([ms, float(e.roomalert_humidity)])
        data_arrays['dome_temp'].append([ms, float(e.dome_temp)])
        data_arrays['dome_humidity'].append([ms, float(e.dome_humidity)])
        data_arrays['underfloor_temp'].append([ms, float(e.underfloor_temp)])
        data_arrays['underfloor_humidity'].append([ms, float(e.underfloor_humidity)])
        data_arrays['truss_temp'].append([ms, float(e.truss_temp)])

    return JsonResponse(json, safe=False)
