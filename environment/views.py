from django.shortcuts import render
from .models import ExternalEnvironmentMeasurement, InternalEnvironmentMeasurement

# Create your views here.

def index(request):
	context = {}
	return render(request, 'environment/environment.html', context)

