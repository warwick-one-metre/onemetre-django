from django.core.management.base import BaseCommand
from environment.models import NITESRoomAlertMeasurement
from environment.management.helpers import RoomAlertHelpers
from datetime import datetime, timezone

class Command(BaseCommand):
    help = 'Queries the NITES Room Alert and inserts a new environment measurement into the database'

    roomalert_ip = '192.168.0.44'
    dummy_json_url = 'http://localhost/static/testdata/nites-roomalert'
    query_timeout = 2.0

    def handle(self, *args, **options):
        try:
#            data = RoomAlertHelpers.query_dummy_json(self.roomalert_url, self.query_timeout)
            data = RoomAlertHelpers.query_roomalert_json(self.roomalert_ip, self.query_timeout)

            parsed_roomalert_time = datetime.strptime(data['date'], "%m/%d/%y %H:%M:%S")
            measurement = NITESRoomAlertMeasurement(
                time = datetime.now().replace(tzinfo=timezone.utc),
                roomalert_time = parsed_roomalert_time.replace(tzinfo=timezone.utc),
                roomalert_internal_temp = data['sensor'][0]['tempc'],
                roomalert_internal_humidity = data['sensor'][0]['humid'],

                internal_temp = data['sensor'][1]['tempc'],
                centre_temp = data['sensor'][2]['tempc'],
                centre_humidity = data['sensor'][2]['humid'],
                dome_open = data['switch_sen'][0]['enabled']
            )

            measurement.save()

        except Exception as e:
            # TODO: Write exception into the database
            print("Query failed with error: " + str(e))

