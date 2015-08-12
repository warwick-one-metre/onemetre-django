from django.contrib import admin
from .models import ExternalEnvironmentMeasurement, InternalEnvironmentMeasurement, NITESRoomAlertMeasurement

class ExternalEnvironmentMeasurementAdmin(admin.ModelAdmin):
	list_display = ('time', 'wind_speed', 'wind_direction', 'air_temperature', 'air_humidity', 'air_pressure', 'rain_amount', 'heater_temperature', 'heater_voltage')

class InternalEnvironmentMeasurementAdmin(admin.ModelAdmin):
	list_display = ('time', 'roomalert_temp', 'roomalert_humidity', 'dome_temp', 'dome_humidity', 'underfloor_temp', 'underfloor_humidity', 'truss_temp')

class NITESRoomAlertMeasurementAdmin(admin.ModelAdmin):
	list_display = ('time', 'roomalert_time', 'roomalert_internal_temp', 'roomalert_internal_humidity', 'internal_temp', 'centre_temp', 'centre_humidity', 'dome_open')

# Register your models here.
admin.site.register(ExternalEnvironmentMeasurement, ExternalEnvironmentMeasurementAdmin)
admin.site.register(InternalEnvironmentMeasurement, InternalEnvironmentMeasurementAdmin)
admin.site.register(NITESRoomAlertMeasurement, NITESRoomAlertMeasurementAdmin)
