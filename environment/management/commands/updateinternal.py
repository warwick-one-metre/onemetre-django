from django.core.management.base import BaseCommand, CommandError
from environment.models import InternalEnvironmentMeasurement
from datetime import datetime
from enum import Enum
import subprocess

class Command(BaseCommand):
    help = 'Queries the Room Alert and inserts a new environment measurement into the database'

    ROOMALERT_IP_ADDRESS = '137.205.160.16'

    class RoomAlertQuery:
        InternalTemperature = '.1.3.6.1.4.1.20916.1.8.1.1.1.2.0'
        InternalHumidity = '.1.3.6.1.4.1.20916.1.8.1.1.2.1.0'
        DomeTemperature = '.1.3.6.1.4.1.20916.1.8.1.2.1.1.0'
        DomeHumidity = '.1.3.6.1.4.1.20916.1.8.1.2.1.3.0'
        UnderFloorTemperature = '.1.3.6.1.4.1.20916.1.8.1.2.2.1.0'
        UnderFloorHumidity = '.1.3.6.1.4.1.20916.1.8.1.2.2.3.0'
        TrussTemperature = '.1.3.6.1.4.1.20916.1.8.1.2.3.1.0'

    def query_float(self, oid):
        output = subprocess.check_output(['/usr/bin/snmpget', '-v', '1', '-c', 'public', self.ROOMALERT_IP_ADDRESS, oid], universal_newlines=True, timeout=5)

        # Output string is of the form '<OID-like-string> = INTEGER: <value>'.  We only care about the final integer value, which is 100 * floating point result
        return int(output.split(' ')[-1]) / 100.0

    def handle(self, *args, **options):

        measurement = InternalEnvironmentMeasurement(
            time = datetime.now(),
            roomalert_temp = self.query_float(Command.RoomAlertQuery.InternalTemperature),
            roomalert_humidity = self.query_float(Command.RoomAlertQuery.InternalHumidity),
            dome_temp = self.query_float(Command.RoomAlertQuery.DomeTemperature),
            dome_humidity = self.query_float(Command.RoomAlertQuery.DomeHumidity),
            underfloor_temp = self.query_float(Command.RoomAlertQuery.UnderFloorTemperature),
            underfloor_humidity = self.query_float(Command.RoomAlertQuery.UnderFloorHumidity),
            truss_temp = self.query_float(Command.RoomAlertQuery.TrussTemperature)
        )

        measurement.save()
