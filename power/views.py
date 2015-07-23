from django.shortcuts import render
from .models import PowerMeasurement

# Create your views here.

def index(request):
	latest_power = PowerMeasurement.objects.latest()
	context = {'latest_power': latest_power}
	return render(request, 'power/power.html', context)
