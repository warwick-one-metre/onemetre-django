from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime, timezone
from enum import Enum
import time
from .models import *

# Create your views here.

def index(request):
    sqt_roomalert = SQTRoomAlertMeasurement.objects.latest()
    nites_roomalert = NITESRoomAlertMeasurement.objects.latest()
    swasp_roomalert = SWASPRoomAlertMeasurement.objects.latest()
    context = {
        'sqt_roomalert': sqt_roomalert,
        'nites_roomalert': nites_roomalert,
        'swasp_roomalert': swasp_roomalert
    }

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
    reference_time = datetime.utcnow().replace(tzinfo=timezone.utc)

    json = {}
    json['reference_time'] = int(time.mktime(reference_time.timetuple()))
    json['axis_label'] = 'Temperature (&deg;C)'
    json['blocks'] = [
        build_block(reference_time, SQTRoomAlertMeasurement.plot_temperature_curves, SQTRoomAlertMeasurement.objects.all()),
        build_block(reference_time, ExternalEnvironmentMeasurement.plot_temperature_curves, ExternalEnvironmentMeasurement.objects.all()),
        build_block(reference_time, NITESRoomAlertMeasurement.plot_temperature_curves, NITESRoomAlertMeasurement.objects.all()),
        build_block(reference_time, SWASPRoomAlertMeasurement.plot_temperature_curves, SWASPRoomAlertMeasurement.objects.all()),
    ]



    return JsonResponse(json)


def json_humidity(request):
    reference_time = datetime.utcnow().replace(tzinfo=timezone.utc)

    json = {}
    json['reference_time'] = int(time.mktime(reference_time.timetuple()))
    json['axis_label'] = 'Relative Humidity (%)'
    json['blocks'] = [
        build_block(reference_time, SQTRoomAlertMeasurement.plot_humidity_curves, SQTRoomAlertMeasurement.objects.all()),
        build_block(reference_time, ExternalEnvironmentMeasurement.plot_humidity_curves, ExternalEnvironmentMeasurement.objects.all()),
        build_block(reference_time, NITESRoomAlertMeasurement.plot_humidity_curves, NITESRoomAlertMeasurement.objects.all()),
        build_block(reference_time, SWASPRoomAlertMeasurement.plot_humidity_curves, SWASPRoomAlertMeasurement.objects.all()),
    ]

    return JsonResponse(json)
