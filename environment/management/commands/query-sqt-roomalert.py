from django.core.management.base import BaseCommand
from environment.models import SQTRoomAlertMeasurement
from environment.management.helpers import RoomAlertHelpers
from datetime import datetime, timezone

class Command(BaseCommand):
    help = 'Queries the SQT Room Alert and inserts a new environment measurement into the database'

    roomalert_ip = '192.168.0.47'
    dummy_json_url = 'http://localhost/static/testdata/sqt-roomalert'
    query_timeout = 2.0

    def handle(self, *args, **options):
        try:
#            data = RoomAlertHelpers.query_dummy_json(self.roomalert_url, self.query_timeout)
            data = RoomAlertHelpers.query_roomalert_json(self.roomalert_ip, self.query_timeout)

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
