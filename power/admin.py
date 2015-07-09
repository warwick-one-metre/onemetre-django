from django.contrib import admin
from .models import PowerMeasurement

class PowerMeasurementAdmin(admin.ModelAdmin):
	list_display = ('time', 'main_ups_status', 'main_ups_battery', 'main_ups_load', 'dome_ups_status', 'dome_ups_battery', 'dome_ups_load')

admin.site.register(PowerMeasurement, PowerMeasurementAdmin)
