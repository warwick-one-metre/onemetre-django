from django.core.management.base import BaseCommand
from environment.models import SWASPRoomAlertMeasurement
from datetime import datetime, timezone
import requests
import demjson
import json

class Command(BaseCommand):
    help = 'Queries the NITES Room Alert and inserts a new environment measurement into the database'

#   roomalert_url = 'http://192.168.0.46/getData.htm'
    roomalert_url = 'http://localhost/static/testdata/swasp-roomalert'
    query_timeout = 2.0

    def handle(self, *args, **options):
        try:
            r = requests.get(self.roomalert_url, timeout=self.query_timeout)
            if r.status_code != requests.codes.ok:
                message = 'Invalid http status: ' + str(r.status_code) + '. ' + \
                          'Query was: `' + self.roomalert_url + '`. ' + \
                          'Response header was: ' + str(r.headers) + '.'
                raise Exception(message)

            # The room alert response is invalid JSON, but demjson can parse it.
            data = demjson.decode(r.text)

            parsed_roomalert_time = datetime.strptime(data['date'], "%m/%d/%y %H:%M:%S")
            measurement = SWASPRoomAlertMeasurement(
                time = datetime.now().replace(tzinfo=timezone.utc),
                roomalert_time = parsed_roomalert_time.replace(tzinfo=timezone.utc),
                roomalert_internal_temp = data['sensor'][0]['tempc'],
                roomalert_internal_humidity = data['sensor'][0]['humid'],

                rack_temp = data['sensor'][1]['tempc'],
                rack_humidity = data['sensor'][1]['humid'],
                computer_room_temp = data['sensor'][3]['tempc'],
                computer_room_humidity = data['sensor'][3]['humid'],

                aircon_airflow = data['switch_sen'][0]['enabled'],
                roof_position = data['switch_sen'][1]['enabled'],
                roof_power = data['switch_sen'][2]['enabled']
            )

            measurement.save()

        except Exception as e:
            # TODO: Write exception into the database
            print("Query failed with error: " + str(e))

