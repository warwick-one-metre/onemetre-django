from django.core.management.base import BaseCommand
from environment.models import SWASPRoomAlertMeasurement
from environment.management.helpers import RoomAlertHelpers
from datetime import datetime, timezone

class Command(BaseCommand):
    help = 'Queries the SWASP Room Alert and inserts a new environment measurement into the database'

    roomalert_ip = '192.168.0.46'
    dummy_json_url = 'http://localhost/static/testdata/swasp-roomalert'
    query_timeout = 2.0

    def handle(self, *args, **options):
        try:
#            data = RoomAlertHelpers.query_dummy_json(self.roomalert_url, self.query_timeout)
            data = RoomAlertHelpers.query_roomalert_json(self.roomalert_ip, self.query_timeout)

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

