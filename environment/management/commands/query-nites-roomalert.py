from django.core.management.base import BaseCommand
from environment.models import NITESRoomAlertMeasurement
from datetime import datetime, timezone
import requests
import demjson

class Command(BaseCommand):
    help = 'Queries the NITES Room Alert and inserts a new environment measurement into the database'

#   roomalert_url = 'http://192.168.0.44/getData.htm'
    roomalert_url = 'http://localhost/static/testdata/nites-roomalert'
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
            # TODO: Upgrading the room alert firmware fixes this and adds more useful stats (like uptime)
            data = demjson.decode(r.text)

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

