from django.contrib import admin
from .models import PowerMeasurement

class PowerMeasurementAdmin(admin.ModelAdmin):
	list_display = ('time', 'main_ups_status', 'main_ups_battery', 'main_ups_load', 'dome_ups_status', 'dome_ups_battery', 'dome_ups_load',
		'roomalert_powered', 'pdu_nominal_computer', 'pdu_telescope_12v_power', 'pdu_telescope_80v_power', 'pdu_webcam_power',
		'pdu_telescope_mixed_power','pdu_cover_motors', 'pdu_light', 'pdu_redundant_computer', 'pdu_dome_controler', 'pdu_dome_power')

admin.site.register(PowerMeasurement, PowerMeasurementAdmin)
