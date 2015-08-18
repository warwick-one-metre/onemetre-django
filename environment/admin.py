from django.contrib import admin
from .models import *

class SQTVaisalaMeasurementAdmin(admin.ModelAdmin):
	list_display = SQTVaisalaMeasurement._meta.get_all_field_names()

class SQTRoomAlertMeasurementAdmin(admin.ModelAdmin):
	list_display = SQTRoomAlertMeasurement._meta.get_all_field_names()

class NITESRoomAlertMeasurementAdmin(admin.ModelAdmin):
	list_display = NITESRoomAlertMeasurement._meta.get_all_field_names()

class SWASPRoomAlertMeasurementAdmin(admin.ModelAdmin):
	list_display = SWASPRoomAlertMeasurement._meta.get_all_field_names()

class SWASPWXDMeasurementAdmin(admin.ModelAdmin):
	list_display = SWASPWXDMeasurement._meta.get_all_field_names()

# Register your models here.
admin.site.register(SQTVaisalaMeasurement, SQTVaisalaMeasurementAdmin)
admin.site.register(SQTRoomAlertMeasurement, SQTRoomAlertMeasurementAdmin)
admin.site.register(NITESRoomAlertMeasurement, NITESRoomAlertMeasurementAdmin)
admin.site.register(SWASPRoomAlertMeasurement, SWASPRoomAlertMeasurementAdmin)
admin.site.register(SWASPWXDMeasurement, SWASPWXDMeasurementAdmin)
