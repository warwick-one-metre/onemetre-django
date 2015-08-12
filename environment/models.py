from django.db import models

# The Vaisala weather station on the LN2 plant
class ExternalEnvironmentMeasurement(models.Model):
	time = models.DateTimeField()
	wind_speed = models.DecimalField(max_digits=5, decimal_places=1)
	wind_direction = models.DecimalField(max_digits=3, decimal_places=0)
	air_temperature = models.DecimalField(max_digits=4, decimal_places=1)
	air_humidity = models.DecimalField(max_digits=4, decimal_places=1)
	air_pressure = models.DecimalField(max_digits=5, decimal_places=1)
	rain_amount = models.DecimalField(max_digits=6, decimal_places=2)
	heater_temperature = models.DecimalField(max_digits=4, decimal_places=1)
	heater_voltage = models.DecimalField(max_digits=4, decimal_places=1)

	class Meta:
		get_latest_by = "time"

# The room alert in the 1m dome
class SQTRoomAlertMeasurement(models.Model):
	time = models.DateTimeField()

	roomalert_time = models.DateTimeField()
	roomalert_internal_temp = models.DecimalField(max_digits=5, decimal_places=2)
	roomalert_internal_humidity = models.DecimalField(max_digits=5, decimal_places=2)
	roomalert_powered = models.BooleanField()

	internal_temp = models.DecimalField(max_digits=5, decimal_places=2)
	internal_humidity = models.DecimalField(max_digits=5, decimal_places=2)
	external_temp = models.DecimalField(max_digits=5, decimal_places=2)
	external_humidity = models.DecimalField(max_digits=5, decimal_places=2)
	truss_temp = models.DecimalField(max_digits=5, decimal_places=2)

	class Meta:
		get_latest_by = "time"

# The room alert in the 40cm dome
class NITESRoomAlertMeasurement(models.Model):
	time = models.DateTimeField()

	roomalert_time = models.DateTimeField()
	roomalert_internal_temp = models.DecimalField(max_digits=5, decimal_places=2)
	roomalert_internal_humidity = models.DecimalField(max_digits=5, decimal_places=2)

	internal_temp = models.DecimalField(max_digits=5, decimal_places=2)

	centre_temp = models.DecimalField(max_digits=5, decimal_places=2)
	centre_humidity = models.DecimalField(max_digits=5, decimal_places=2)

	dome_open = models.BooleanField()

	class Meta:
		get_latest_by = "time"

# The room alert in the swasp dome
class SWASPRoomAlertMeasurement(models.Model):
    time = models.DateTimeField()

    roomalert_time = models.DateTimeField()
    roomalert_internal_temp = models.DecimalField(max_digits=5, decimal_places=2)
    roomalert_internal_humidity = models.DecimalField(max_digits=5, decimal_places=2)

    rack_temp = models.DecimalField(max_digits=5, decimal_places=2)
    rack_humidity = models.DecimalField(max_digits=5, decimal_places=2)

    computer_room_temp = models.DecimalField(max_digits=5, decimal_places=2)
    computer_room_humidity = models.DecimalField(max_digits=5, decimal_places=2)

    aircon_airflow = models.BooleanField()
    roof_position = models.BooleanField()
    roof_power = models.BooleanField()

    class Meta:
        get_latest_by = "time"

