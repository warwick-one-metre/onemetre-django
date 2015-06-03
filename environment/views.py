from django.shortcuts import render
from .models import ExternalEnvironmentMeasurement, InternalEnvironmentMeasurement

# Create your views here.

def index(request):
	latest_internal = ExternalEnvironmentMeasurement.objects.latest()

	context = {
		'latest_internal': latest_internal,
	}

	return render(request, 'environment/index.html', context)

