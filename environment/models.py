from django.db import models

# The Vaisala weather station on the LN2 plant
class SQTVaisalaMeasurement(models.Model):
    bin_time = models.DateTimeField()
    time_min = models.DateTimeField()
    time_max = models.DateTimeField()

    wind_speed_min = models.DecimalField(max_digits=5, decimal_places=1)
    wind_speed_max = models.DecimalField(max_digits=5, decimal_places=1)
    wind_direction_min = models.DecimalField(max_digits=3, decimal_places=0)
    wind_direction_max = models.DecimalField(max_digits=3, decimal_places=0)
    air_temperature_min = models.DecimalField(max_digits=4, decimal_places=1)
    air_temperature_max = models.DecimalField(max_digits=4, decimal_places=1)
    air_humidity_min = models.DecimalField(max_digits=4, decimal_places=1)
    air_humidity_max = models.DecimalField(max_digits=4, decimal_places=1)
    air_pressure_min = models.DecimalField(max_digits=5, decimal_places=1)
    air_pressure_max = models.DecimalField(max_digits=5, decimal_places=1)
    rain_amount_min = models.DecimalField(max_digits=6, decimal_places=2)
    rain_amount_max = models.DecimalField(max_digits=6, decimal_places=2)
    heater_temperature_min = models.DecimalField(max_digits=4, decimal_places=1)
    heater_temperature_max = models.DecimalField(max_digits=4, decimal_places=1)
    heater_voltage_min = models.DecimalField(max_digits=4, decimal_places=1)
    heater_voltage_max = models.DecimalField(max_digits=4, decimal_places=1)

    plot_temperature_curves = (
        ('air_temperature_min', 'Vaisala'),
    )

    plot_humidity_curves = (
        ('air_humidity_min', 'Vaisala'),
    )

    class Meta:
        get_latest_by = "bin_time"

# The room alert in the 1m dome
class SQTRoomAlertMeasurement(models.Model):
    bin_time = models.DateTimeField()

    roomalert_time_min = models.DateTimeField()
    roomalert_time_max = models.DateTimeField()
    roomalert_internal_temp_min = models.DecimalField(max_digits=5, decimal_places=2)
    roomalert_internal_temp_max = models.DecimalField(max_digits=5, decimal_places=2)
    roomalert_internal_humidity_min = models.DecimalField(max_digits=5, decimal_places=2)
    roomalert_internal_humidity_max = models.DecimalField(max_digits=5, decimal_places=2)
    roomalert_powered = models.BooleanField()

    internal_temp_min = models.DecimalField(max_digits=5, decimal_places=2)
    internal_temp_max = models.DecimalField(max_digits=5, decimal_places=2)
    internal_humidity_min = models.DecimalField(max_digits=5, decimal_places=2)
    internal_humidity_max = models.DecimalField(max_digits=5, decimal_places=2)
    external_temp_min = models.DecimalField(max_digits=5, decimal_places=2)
    external_temp_max = models.DecimalField(max_digits=5, decimal_places=2)
    external_humidity_min = models.DecimalField(max_digits=5, decimal_places=2)
    external_humidity_max = models.DecimalField(max_digits=5, decimal_places=2)
    truss_temp_min = models.DecimalField(max_digits=5, decimal_places=2)
    truss_temp_max = models.DecimalField(max_digits=5, decimal_places=2)

    plot_temperature_curves = (
        ('roomalert_internal_temp_min', 'SQT Room Alert'),
        ('internal_temp_min', 'SQT Dome'),
        ('external_temp_min', 'SQT Outside'),
        ('truss_temp_min', 'SQT Truss'),
    )

    plot_humidity_curves = (
        ('roomalert_internal_humidity_min', 'SQT Room Alert'),
        ('internal_humidity_min', 'SQT Dome'),
        ('external_humidity_min', 'SQT Outside'),
    )

    def latest_measurement_json():
        latest = SQTRoomAlertMeasurement.objects.latest()
        return {
            'updated': 'Updated ' + latest.time.strftime('%Y-%d-%m %H:%M:%S'),
            'roomalert': '%s &#8451;<br />%s %% RH' % (latest.roomalert_internal_temp_min, latest.roomalert_internal_humidity_min),
            'dome': '%s &#8451;<br />%s %% RH' % (latest.internal_temp_min, latest.internal_humidity_min),
            'outside': '%s &#8451;<br />%s %% RH' % (latest.external_temp_min, latest.external_humidity_min),
            'truss': '%s &#8451;' % latest.external_temp_min,
            'trap_open': '<span style="color: #FFA500">UNKNOWN</span>',
            'hatch_open': '<span style="color: #FFA500">UNKNOWN</span>',
            'dome_open': '<span style="color: #FFA500">UNKNOWN</span>',
            'covers_open': '<span style="color: #FFA500">UNKNOWN</span>',
        }

    class Meta:
        get_latest_by = "bin_time"

# The room alert in the 40cm dome
class NITESRoomAlertMeasurement(models.Model):
    bin_time = models.DateTimeField()

    roomalert_time_min = models.DateTimeField()
    roomalert_time_max = models.DateTimeField()
    roomalert_internal_temp_min = models.DecimalField(max_digits=5, decimal_places=2)
    roomalert_internal_temp_max = models.DecimalField(max_digits=5, decimal_places=2)
    roomalert_internal_humidity_min = models.DecimalField(max_digits=5, decimal_places=2)
    roomalert_internal_humidity_max = models.DecimalField(max_digits=5, decimal_places=2)

    internal_temp_min = models.DecimalField(max_digits=5, decimal_places=2)
    internal_temp_max = models.DecimalField(max_digits=5, decimal_places=2)

    centre_temp_min = models.DecimalField(max_digits=5, decimal_places=2)
    centre_temp_max = models.DecimalField(max_digits=5, decimal_places=2)
    centre_humidity_min = models.DecimalField(max_digits=5, decimal_places=2)
    centre_humidity_max = models.DecimalField(max_digits=5, decimal_places=2)

    dome_open = models.BooleanField()

    plot_temperature_curves = (
        ('roomalert_internal_temp_min', 'NITES Room Alert'),
        ('centre_temp_min', 'NITES Dome'),
    )

    plot_humidity_curves = (
        ('roomalert_internal_humidity_min', 'NITES Room Alert'),
        ('centre_humidity_min', 'NITES Dome'),
    )

    def latest_measurement_json():
        latest = NITESRoomAlertMeasurement.objects.latest()
        dome_html = '<span style="color: #090">OPEN</span>' if latest.dome_open else '<span style="color: #C00">CLOSED</span>'
        return {
            'updated': 'Updated ' + latest.time.strftime('%Y-%d-%m %H:%M:%S'),
            'roomalert': '%s &#8451;<br />%s %% RH' % (latest.roomalert_internal_temp_min, latest.roomalert_internal_humidity_min),
            'dome': '%s &#8451;<br />%s %% RH' % (latest.centre_temp_min, latest.centre_humidity_min),
            'internal': '%s &#8451;' % latest.internal_temp_min,
            'dome_open': dome_html,
        }

    class Meta:
        get_latest_by = "bin_time"

# The room alert in the swasp dome
class SWASPRoomAlertMeasurement(models.Model):
    bin_time = models.DateTimeField()

    roomalert_time_min = models.DateTimeField()
    roomalert_time_max = models.DateTimeField()
    roomalert_internal_temp_min = models.DecimalField(max_digits=5, decimal_places=2)
    roomalert_internal_temp_max = models.DecimalField(max_digits=5, decimal_places=2)
    roomalert_internal_humidity_min = models.DecimalField(max_digits=5, decimal_places=2)
    roomalert_internal_humidity_max = models.DecimalField(max_digits=5, decimal_places=2)

    rack_temp_min = models.DecimalField(max_digits=5, decimal_places=2)
    rack_temp_max = models.DecimalField(max_digits=5, decimal_places=2)
    rack_humidity_min = models.DecimalField(max_digits=5, decimal_places=2)
    rack_humidity_max = models.DecimalField(max_digits=5, decimal_places=2)

    computer_room_temp_min = models.DecimalField(max_digits=5, decimal_places=2)
    computer_room_temp_max = models.DecimalField(max_digits=5, decimal_places=2)
    computer_room_humidity_min = models.DecimalField(max_digits=5, decimal_places=2)
    computer_room_humidity_max = models.DecimalField(max_digits=5, decimal_places=2)

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
            'roomalert': '%s &#8451;<br />%s %% RH' % (latest.roomalert_internal_temp_min, latest.roomalert_internal_humidity_min),
            'rack': '%s &#8451;<br />%s %% RH' % (latest.rack_temp_min, latest.rack_humidity_min),
            'computer_room': '%s &#8451;<br />%s %% RH' % (latest.computer_room_temp_min, latest.computer_room_humidity_min),
            'aircon': aircon_html,
            'roof': roof_html,
            'roof_power': roof_power_html,
        }

    class Meta:
        get_latest_by = "bin_time"

# The SWASP weather station, parsed from the wxd log file
class SWASPWXDMeasurement(models.Model):
    bin_time = models.DateTimeField()
    measurement_time_min = models.DateTimeField()
    measurement_time_max = models.DateTimeField()

    wind_speed_min = models.DecimalField(max_digits=5, decimal_places=1)
    wind_speed_max = models.DecimalField(max_digits=5, decimal_places=1)
    wind_direction_min = models.DecimalField(max_digits=3, decimal_places=0)
    wind_direction_max = models.DecimalField(max_digits=3, decimal_places=0)
    inside_temperature_min = models.DecimalField(max_digits=4, decimal_places=1)
    inside_temperature_max = models.DecimalField(max_digits=4, decimal_places=1)
    inside_humidity_min = models.DecimalField(max_digits=4, decimal_places=1)
    inside_humidity_max = models.DecimalField(max_digits=4, decimal_places=1)
    pressure_min = models.DecimalField(max_digits=5, decimal_places=1)
    pressure_max = models.DecimalField(max_digits=5, decimal_places=1)

    rain_wet = models.BooleanField()

    sky_temperature_min = models.DecimalField(max_digits=6, decimal_places=2)
    sky_temperature_max = models.DecimalField(max_digits=6, decimal_places=2)
    outside_temperature_min = models.DecimalField(max_digits=4, decimal_places=1)
    outside_temperature_max = models.DecimalField(max_digits=4, decimal_places=1)
    outside_humidity_min = models.DecimalField(max_digits=4, decimal_places=1)
    outside_humidity_max = models.DecimalField(max_digits=4, decimal_places=1)
    dew_point_min = models.DecimalField(max_digits=4, decimal_places=1)
    dew_point_max = models.DecimalField(max_digits=4, decimal_places=1)

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
            'wind': '%s m/s from %s&deg' % (latest.wind_speed_min, latest.wind_direction_min),
            'inside': '%s &#8451;<br />%s %% RH' % (latest.inside_temperature_min, latest.inside_humidity_min),
            'outside': '%s &#8451;<br />%s %% RH' % (latest.outside_temperature_min, latest.outside_humidity_min),
            'rain': rain_html,
            'pressure': '%s mBar' % latest.pressure,
            'sky_temp': '%s &#8451;' % latest.sky_temperature,
            'dew_point': '%s &#8451;' % latest.dew_point
        }

    class Meta:
        get_latest_by = "bin_time"

