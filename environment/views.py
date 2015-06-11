from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime, timezone
import time
from .models import ExternalEnvironmentMeasurement, InternalEnvironmentMeasurement

# Create your views here.

def index(request):
	context = {}
	return render(request, 'environment/environment.html', context)

def json(request):
    json = []

    # External Temperature
    ext_temp = {}
    ext_temp['label'] = 'External Temperature'
    ext_temp_data = []
    ext_temp['data'] = ext_temp_data
    ext_temp['yaxis'] = 1
    json.append(ext_temp)

    # External Humidity
    ext_humidity = {}
    ext_humidity['label'] = 'External Humidity'
    ext_humidity_data = []
    ext_humidity['data'] = ext_humidity_data
    ext_humidity['yaxis'] = 2
    json.append(ext_humidity)

    # Wind speed
    wind_speed = {}
    wind_speed['label'] = 'Wind Speed'
    wind_speed_data = []
    wind_speed['data'] = wind_speed_data
    wind_speed['yaxis'] = 3
    json.append(wind_speed)

    for e in ExternalEnvironmentMeasurement.objects.all():
        ms = time.mktime(e.time.timetuple()) * 1000
        ext_temp_data.append([ms, float(e.air_temperature)])
        ext_humidity_data.append([ms, float(e.air_humidity)])
        wind_speed_data.append([ms, float(e.wind_speed)])

    return JsonResponse(json, safe=False)