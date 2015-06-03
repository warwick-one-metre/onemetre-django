from django.contrib import admin
from .models import ExternalEnvironmentMeasurement, InternalEnvironmentMeasurement

class ExternalEnvironmentMeasurementAdmin(admin.ModelAdmin):
	list_display = ('time', 'wind_speed', 'wind_direction', 'air_temperature', 'air_humidity', 'air_pressure', 'rain_amount', 'heater_temperature', 'heater_voltage')

class InternalEnvironmentMeasurementAdmin(admin.ModelAdmin):
	list_display = ('time', 'east_dome_open', 'east_dome_closed', 'west_dome_open', 'west_dome_closed', 'hatch_closed', 'trap_closed')


# Register your models here.
admin.site.register(ExternalEnvironmentMeasurement, ExternalEnvironmentMeasurementAdmin)
admin.site.register(InternalEnvironmentMeasurement, InternalEnvironmentMeasurementAdmin)
