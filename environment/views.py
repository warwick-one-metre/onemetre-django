from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime, timezone, timedelta
from enum import Enum
from .models import *
import time

# Create your views here.

def index(request):
    context = {
        'sqt_roomalert': SQTRoomAlertMeasurement.objects.latest(),
#        'sqt_vaisala': SQTVaisalaMeasurement.objects.latest(),
        'nites_roomalert': NITESRoomAlertMeasurement.objects.latest(),
        'swasp_roomalert': SWASPRoomAlertMeasurement.objects.latest()
    }

    return render(request, 'environment/environment.html', context)

def build_block(reference_time, measurement_types, objects):
    queryset = objects.filter(time__gte=(datetime.now() - timedelta(seconds=86400)))
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

def build_temperature_block(reference_time, model):
    return build_block(reference_time, model.plot_temperature_curves, model.objects)

def build_humidity_block(reference_time, model):
    return build_block(reference_time, model.plot_humidity_curves, model.objects)

def json_temperature(request):
    reference_time = datetime.utcnow().replace(tzinfo=timezone.utc)

    json = {}
    json['reference_time'] = int(time.mktime(reference_time.timetuple()))
    json['axis_label'] = 'Temperature (&deg;C)'
    json['blocks'] = [
        build_temperature_block(reference_time, SQTRoomAlertMeasurement),
#        build_temperature_block(reference_time, SQTVaisalaMeasurement),
        build_temperature_block(reference_time, NITESRoomAlertMeasurement),
        build_temperature_block(reference_time, SWASPRoomAlertMeasurement),
        build_temperature_block(reference_time, SWASPWXDMeasurement),
    ]

    return JsonResponse(json)


def json_humidity(request):
    reference_time = datetime.utcnow().replace(tzinfo=timezone.utc)

    json = {}
    json['reference_time'] = int(time.mktime(reference_time.timetuple()))
    json['axis_label'] = 'Relative Humidity (%)'
    json['blocks'] = [
        build_humidity_block(reference_time, SQTRoomAlertMeasurement),
#        build_humidity_block(reference_time, SQTVaisalaMeasurement),
        build_humidity_block(reference_time, NITESRoomAlertMeasurement),
        build_humidity_block(reference_time, SWASPRoomAlertMeasurement),
        build_humidity_block(reference_time, SWASPWXDMeasurement),
    ]

    return JsonResponse(json)

def json_latest(request):
    json = {
        'sqt_roomalert': SQTRoomAlertMeasurement.latest_measurement_json(),
        'nites_roomalert': NITESRoomAlertMeasurement.latest_measurement_json(),
        'swasp_roomalert': SWASPRoomAlertMeasurement.latest_measurement_json(),
        'swasp_wxd': SWASPWXDMeasurement.latest_measurement_json()
    }

    return JsonResponse(json)

