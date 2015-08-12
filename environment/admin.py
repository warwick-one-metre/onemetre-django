from django.contrib import admin
from .models import *

class SQTVaisalaMeasurementAdmin(admin.ModelAdmin):
	list_display = ('time', 'wind_speed', 'wind_direction', 'air_temperature', 'air_humidity', 'air_pressure', 'rain_amount', 'heater_temperature', 'heater_voltage')

class SQTRoomAlertMeasurementAdmin(admin.ModelAdmin):
	list_display = ('time', 'roomalert_time', 'roomalert_internal_temp', 'roomalert_internal_humidity', 'internal_temp', 'internal_humidity', 'external_temp', 'external_humidity', 'truss_temp', 'roomalert_powered')

class NITESRoomAlertMeasurementAdmin(admin.ModelAdmin):
	list_display = ('time', 'roomalert_time', 'roomalert_internal_temp', 'roomalert_internal_humidity', 'internal_temp', 'centre_temp', 'centre_humidity', 'dome_open')

class SWASPRoomAlertMeasurementAdmin(admin.ModelAdmin):
	list_display = ('time', 'roomalert_time', 'roomalert_internal_temp', 'roomalert_internal_humidity', 'rack_temp', 'rack_humidity', 'computer_room_temp', 'computer_room_humidity', 'aircon_airflow', 'roof_position', 'roof_power')

# Register your models here.
admin.site.register(SQTVaisalaMeasurement, SQTVaisalaMeasurementAdmin)
admin.site.register(SQTRoomAlertMeasurement, SQTRoomAlertMeasurementAdmin)
admin.site.register(NITESRoomAlertMeasurement, NITESRoomAlertMeasurementAdmin)
admin.site.register(SWASPRoomAlertMeasurement, SWASPRoomAlertMeasurementAdmin)
