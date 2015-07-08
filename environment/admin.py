from django.contrib import admin
from .models import ExternalEnvironmentMeasurement, InternalEnvironmentMeasurement

class ExternalEnvironmentMeasurementAdmin(admin.ModelAdmin):
	list_display = ('time', 'wind_speed', 'wind_direction', 'air_temperature', 'air_humidity', 'air_pressure', 'rain_amount', 'heater_temperature', 'heater_voltage')

class InternalEnvironmentMeasurementAdmin(admin.ModelAdmin):
	list_display = ('time', 'roomalert_temp', 'roomalert_humidity', 'dome_temp', 'dome_humidity', 'underfloor_temp', 'underfloor_humidity', 'truss_temp')

# Register your models here.
admin.site.register(ExternalEnvironmentMeasurement, ExternalEnvironmentMeasurementAdmin)
admin.site.register(InternalEnvironmentMeasurement, InternalEnvironmentMeasurementAdmin)
