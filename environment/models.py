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

    plot_temperature_curves = (
        ('air_temperature', 'Vaisala'),
    )

    plot_humidity_curves = (
        ('air_humidity', 'Vaisala'),
    )

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

    plot_temperature_curves = (
        ('roomalert_internal_temp', 'SQT Room Alert'),
        ('internal_temp', 'SQT Dome'),
        ('external_temp', 'SQT Outside'),
        ('truss_temp', 'SQT Truss'),
    )

    plot_humidity_curves = (
        ('roomalert_internal_humidity', 'SQT Room Alert'),
        ('internal_humidity', 'SQT Dome'),
        ('external_humidity', 'SQT Outside'),
    )

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

    plot_temperature_curves = (
        ('roomalert_internal_temp', 'NITES Room Alert'),
        ('centre_temp', 'NITES Dome'),
        ('internal_temp', 'NITES Internal'),
    )

    plot_humidity_curves = (
        ('roomalert_internal_humidity', 'NITES Room Alert'),
        ('centre_humidity', 'NITES Dome'),
    )

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

    plot_temperature_curves = (
        ('roomalert_internal_temp', 'SWASP Room Alert'),
        ('rack_temp', 'SWASP Rack'),
        ('computer_room_temp', 'SWASP Computer room'),
    )

    plot_humidity_curves = (
        ('roomalert_internal_humidity', 'SWASP Room Alert'),
        ('rack_humidity', 'SWASP Rack'),
        ('computer_room_humidity', 'SWASP Computer room'),
    )

    class Meta:
        get_latest_by = "time"

