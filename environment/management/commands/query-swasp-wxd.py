from django.core.management.base import BaseCommand
from environment.models import SWASPWXDMeasurement
from datetime import datetime, timezone
from astropy.time import Time
import requests

class Command(BaseCommand):
    help = 'Queries the SWASP WXD log and inserts a new environment measurement into the database'

    log_url = 'http://wasp.warwick.ac.uk/swasp/main/monitor/public/weather.log'
    query_timeout = 2.0

    def handle(self, *args, **options):
        try:
            r = requests.get(self.log_url, timeout=self.query_timeout)
            if r.status_code != requests.codes.ok:
                message = 'Invalid http status: ' + str(r.status_code) + '. ' + \
                    'Query was: `' + self.roomalert_url + '`. ' + \
                    'Response header was: ' + str(r.headers) + '.'
                raise Exception(message)

            data = r.text.splitlines()[-1].split();

            measurement = SWASPWXDMeasurement(
                time = datetime.now().replace(tzinfo=timezone.utc),
                measurement_time = Time(float(data[0]), format='jd', scale='utc').datetime.replace(tzinfo=timezone.utc),
                wind_speed = float(data[1]) / 3.6, # Convert km/h to m/s
                wind_direction = float(data[2]),
                inside_temperature = float(data[3]),
                inside_humidity = float(data[4]),
                pressure = float(data[5]),
                rain_wet = data[7] != 'DRY',
                sky_temperature = float(data[8]),
                outside_temperature = float(data[11]),
                outside_humidity = float(data[14]),
                dew_point = float(data[17]),
            )

            measurement.save()

        except Exception as e:
            # TODO: Write exception into the database
            print("Query failed with error: " + str(e))

