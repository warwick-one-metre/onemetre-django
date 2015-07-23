from django.core.management.base import BaseCommand, CommandError
from power.models import PowerMeasurement
from datetime import datetime, timezone
import subprocess

class Command(BaseCommand):
    help = 'Queries the PDU and device statuses and inserts a new power measurement into the database'

    MAIN_UPS_IP_ADDRESS = '192.168.0.115'
    DOME_UPS_IP_ADDRESS = '192.168.0.116'
    ROOMALERT_IP_ADDRESS = '192.168.0.47'
    MAIN_PDU_IP_ADDRESS = '192.168.0.111'
    SECONDARY_PDU_IP_ADDRESS = '192.168.0.112'

    class PowerQuery:
        UPSStatus = '.1.3.6.1.4.1.318.1.1.1.2.1.1.0'
        UPSBattery = '.1.3.6.1.4.1.318.1.1.1.2.2.1.0'
        UPSLoad = '.1.3.6.1.4.1.318.1.1.1.4.2.3.0'

        RoomAlert = '.1.3.6.1.4.1.20916.1.8.1.1.3.1.0'

        PDUChannel1 = '.1.3.6.1.4.1.318.1.1.12.3.3.1.1.4.1'
        PDUChannel2 = '.1.3.6.1.4.1.318.1.1.12.3.3.1.1.4.2'
        PDUChannel3 = '.1.3.6.1.4.1.318.1.1.12.3.3.1.1.4.3'
        PDUChannel4 = '.1.3.6.1.4.1.318.1.1.12.3.3.1.1.4.4'
        PDUChannel5 = '.1.3.6.1.4.1.318.1.1.12.3.3.1.1.4.5'
        PDUChannel6 = '.1.3.6.1.4.1.318.1.1.12.3.3.1.1.4.6'
        PDUChannel7 = '.1.3.6.1.4.1.318.1.1.12.3.3.1.1.4.7'
        PDUChannel8 = '.1.3.6.1.4.1.318.1.1.12.3.3.1.1.4.8'


    def query_bool(self, ip,query):
        output = subprocess.check_output(['/usr/bin/snmpget', '-v', '1', '-c', 'public', ip, query], universal_newlines=True, timeout=5)

        # Output string is of the form '<OID-like-string> = INTEGER: <value>'.  We only care about the final integer value, which is 1 if true, 2 if false
        return output.split(' ')[-1] == '1'

    def handle(self, *args, **options):

        measurement = PowerMeasurement(
            time = datetime.now().replace(tzinfo=timezone.utc),

            main_ups_status = self.query_bool(self.MAIN_UPS_IP_ADDRESS, Command.PowerQuery.UPSStatus),
            main_ups_battery = self.query_bool(self.MAIN_UPS_IP_ADDRESS, Command.PowerQuery.UPSBattery),
            main_ups_load = self.query_bool(self.MAIN_UPS_IP_ADDRESS, Command.PowerQuery.UPSLoad),

            dome_ups_status = self.query_bool(self.DOME_UPS_IP_ADDRESS, Command.PowerQuery.UPSStatus),
            dome_ups_battery = self.query_bool(self.DOME_UPS_IP_ADDRESS, Command.PowerQuery.UPSBattery),
            dome_ups_load = self.query_bool(self.DOME_UPS_IP_ADDRESS, Command.PowerQuery.UPSLoad),

            roomalert_powered = self.query_bool(self.ROOMALERT_PDU_IP_ADDRESS, Command.PowerQuery.RoomAlert),

            pdu_nominal_computer = self.query_bool(self.MAIN_PDU_IP_ADDRESS, Command.PowerQuery.PDUChannel1),
            pdu_telescope_12v_power = self.query_bool(self.MAIN_PDU_IP_ADDRESS, Command.PowerQuery.PDUChannel2),
            pdu_telescope_80v_power = self.query_bool(self.MAIN_PDU_IP_ADDRESS, Command.PowerQuery.PDUChannel3),
            pdu_webcam_power = self.query_bool(self.MAIN_PDU_IP_ADDRESS, Command.PowerQuery.PDUChannel4),
            pdu_telescope_mixed_power = self.query_bool(self.MAIN_PDU_IP_ADDRESS, Command.PowerQuery.PDUChannel5),
            pdu_cover_motors = self.query_bool(self.MAIN_PDU_IP_ADDRESS, Command.PowerQuery.PDUChannel6),
            pdu_light = self.query_bool(self.MAIN_PDU_IP_ADDRESS, Command.PowerQuery.PDUChannel8),
            pdu_redundant_computer = self.query_bool(self.SECONDARY_PDU_IP_ADDRESS, Command.PowerQuery.PDUChannel1),
            pdu_dome_controler = self.query_bool(self.SECONDARY_PDU_IP_ADDRESS, Command.PowerQuery.PDUChannel2),
            pdu_dome_power = self.query_bool(self.SECONDARY_PDU_IP_ADDRESS, Command.PowerQuery.PDUChannel3),
        )

        measurement.save()
