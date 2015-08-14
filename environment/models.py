from django.db import models

# The Vaisala weather station on the LN2 plant
class SQTVaisalaMeasurement(models.Model):
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

    def latest_measurement_json():
        latest = SQTRoomAlertMeasurement.objects.latest()
        return {
            'updated': 'Updated ' + latest.time.strftime('%Y-%d-%m %H:%M:%S'),
            'roomalert': '%s &#8451;<br />%s %% RH' % (latest.roomalert_internal_temp, latest.roomalert_internal_humidity),
            'dome': '%s &#8451;<br />%s %% RH' % (latest.internal_temp, latest.internal_humidity),
            'outside': '%s &#8451;<br />%s %% RH' % (latest.external_temp, latest.external_humidity),
            'truss': '%s &#8451;' % latest.external_temp,
            'trap_open': '<span style="color: #FFA500">UNKNOWN</span>',
            'hatch_open': '<span style="color: #FFA500">UNKNOWN</span>',
            'dome_open': '<span style="color: #FFA500">UNKNOWN</span>',
            'covers_open': '<span style="color: #FFA500">UNKNOWN</span>',
        }

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
    )

    plot_humidity_curves = (
        ('roomalert_internal_humidity', 'NITES Room Alert'),
        ('centre_humidity', 'NITES Dome'),
    )

    def latest_measurement_json():
        latest = NITESRoomAlertMeasurement.objects.latest()
        dome_html = '<span style="color: #090">OPEN</span>' if latest.dome_open else '<span style="color: #C00">CLOSED</span>'
        return {
            'updated': 'Updated ' + latest.time.strftime('%Y-%d-%m %H:%M:%S'),
            'roomalert': '%s &#8451;<br />%s %% RH' % (latest.roomalert_internal_temp, latest.roomalert_internal_humidity),
            'dome': '%s &#8451;<br />%s %% RH' % (latest.centre_temp, latest.centre_humidity),
            'internal': '%s &#8451;' % latest.internal_temp,
            'dome_open': dome_html,
        }

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

    plot_temperature_curves = ()

    plot_humidity_curves = ()

    def latest_measurement_json():
        latest = SWASPRoomAlertMeasurement.objects.latest()
        aircon_html = '<span style="color: #090">ON</span>' if latest.aircon_airflow else '<span style="color: #C00">OFF</span>'
        roof_html = '<span style="color: #C00">CLOSED</span>' if latest.roof_position else '<span style="color: #090">OPEN</span>'
        roof_power_html = '<span style="color: #090">ON</span>' if latest.roof_power else '<span style="color: #C00">OFF</span>'
        return {
            'updated': 'Updated ' + latest.time.strftime('%Y-%d-%m %H:%M:%S'),
            'roomalert': '%s &#8451;<br />%s %% RH' % (latest.roomalert_internal_temp, latest.roomalert_internal_humidity),
            'rack': '%s &#8451;<br />%s %% RH' % (latest.rack_temp, latest.rack_humidity),
            'computer_room': '%s &#8451;<br />%s %% RH' % (latest.computer_room_temp, latest.computer_room_humidity),
            'aircon': aircon_html,
            'roof': roof_html,
            'roof_power': roof_power_html,
        }

    class Meta:
        get_latest_by = "time"

# The SWASP weather station, parsed from the wxd log file
class SWASPWXDMeasurement(models.Model):
    time = models.DateTimeField()
    measurement_time = models.DateTimeField()

    wind_speed = models.DecimalField(max_digits=5, decimal_places=1)
    wind_direction = models.DecimalField(max_digits=3, decimal_places=0)
    inside_temperature = models.DecimalField(max_digits=4, decimal_places=1)
    inside_humidity = models.DecimalField(max_digits=4, decimal_places=1)
    pressure = models.DecimalField(max_digits=5, decimal_places=1)
    rain_wet = models.BooleanField()
    sky_temperature = models.DecimalField(max_digits=6, decimal_places=2)
    outside_temperature = models.DecimalField(max_digits=4, decimal_places=1)
    outside_humidity = models.DecimalField(max_digits=4, decimal_places=1)
    dew_point = models.DecimalField(max_digits=4, decimal_places=1)

    plot_temperature_curves = (
        ('outside_temperature', 'SWASP Weather Station'),
        ('dew_point', 'SWASP Dew Point'),
    )

    plot_humidity_curves = (
        ('outside_humidity', 'SWASP Weather Station'),
    )

    def latest_measurement_json():
        latest = SWASPWXDMeasurement.objects.latest()
        rain_html = '<span style="color: #C00">WET</span>' if latest.rain_wet else '<span style="color: #090">DRY</span>'
        return {
            'updated': 'Updated ' + latest.time.strftime('%Y-%d-%m %H:%M:%S'),
            'wind': '%s m/s from %s&deg' % (latest.wind_speed, latest.wind_direction),
            'inside': '%s &#8451;<br />%s %% RH' % (latest.inside_temperature, latest.inside_humidity),
            'outside': '%s &#8451;<br />%s %% RH' % (latest.outside_temperature, latest.outside_humidity),
            'rain': rain_html,
            'pressure': '%s mBar' % latest.pressure,
            'sky_temp': '%s &#8451;' % latest.sky_temperature,
            'dew_point': '%s &#8451;' % latest.dew_point
        }

    class Meta:
        get_latest_by = "time"

