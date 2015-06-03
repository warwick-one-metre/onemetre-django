from django.db import models

# Create your models here.

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

class InternalEnvironmentMeasurement(models.Model):
	time = models.DateTimeField()
	east_dome_open = models.BooleanField()
	east_dome_closed = models.BooleanField()
	west_dome_open = models.BooleanField()
	west_dome_closed = models.BooleanField()
	hatch_closed = models.BooleanField()
	trap_closed = models.BooleanField()

	class Meta:
		get_latest_by = "time"
