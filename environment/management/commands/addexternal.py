from django.core.management.base import BaseCommand, CommandError
from environment.models import SQTVaisalaMeasurement
from datetime import datetime
from pytz import UTC, timezone

class Command(BaseCommand):
    help = 'Inserts a new external environment measurement into the database'

    def add_arguments(self, parser):
        parser.add_argument('date')
        parser.add_argument('time')

        parser.add_argument('wind_speed', type=float)
        parser.add_argument('wind_direction', type=float)
        parser.add_argument('air_temperature', type=float)
        parser.add_argument('air_humidity', type=float)
        parser.add_argument('air_pressure', type=float)
        parser.add_argument('rain_amount', type=float)
        parser.add_argument('heater_temperature', type=float)
        parser.add_argument('heater_voltage', type=float)

    def handle(self, *args, **options):
        dt = options['date'] + ' ' + options['time']

        measurement = SQTVaisalaMeasurement(
            time = UTC.localize(datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')),
            wind_speed = options['wind_speed'],
            wind_direction = options['wind_direction'],
            air_temperature = options['air_temperature'],
            air_humidity = options['air_humidity'],
            air_pressure = options['air_pressure'],
            rain_amount = options['rain_amount'],
            heater_temperature = options['heater_temperature'],
            heater_voltage = options['heater_voltage']
        )
        
        measurement.save()
