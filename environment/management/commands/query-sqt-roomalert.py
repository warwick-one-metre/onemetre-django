from django.core.management.base import BaseCommand
from environment.models import SQTRoomAlertMeasurement
from datetime import datetime, timezone
import requests

class Command(BaseCommand):
    help = 'Queries the SQT Room Alert and inserts a new environment measurement into the database'

#   roomalert_url = 'http://192.168.0.47/getData.htm'
    roomalert_url = 'http://localhost/static/testdata/sqt-roomalert'
    query_timeout = 2.0

    def handle(self, *args, **options):
        try:
            r = requests.get(self.roomalert_url, timeout=self.query_timeout)
            if r.status_code != requests.codes.ok:
                message = 'Invalid http status: ' + str(r.status_code) + '. ' + \
                          'Query was: `' + self.roomalert_url + '`. ' + \
                          'Response header was: ' + str(r.headers) + '.'
                raise Exception(message)

            data = r.json()

            parsed_roomalert_time = datetime.strptime(data['date'], "%m/%d/%y %H:%M:%S")
            measurement = SQTRoomAlertMeasurement(
                time = datetime.now().replace(tzinfo=timezone.utc),
                roomalert_time = parsed_roomalert_time.replace(tzinfo=timezone.utc),
                roomalert_internal_temp = data['internal_sen'][0]['tc'],
                roomalert_internal_humidity = data['internal_sen'][0]['h'],
                roomalert_powered = data['internal_sen'][3]['stat'],

                internal_temp = data['sensor'][0]['tc'],
                internal_humidity = data['sensor'][0]['h'],
                external_temp = data['sensor'][1]['tc'],
                external_humidity = data['sensor'][1]['h'],
                truss_temp = data['sensor'][2]['tc']
            )

            measurement.save()

        except Exception as e:
            # TODO: Write exception into the database
            print("Query failed with error: " + str(e))
