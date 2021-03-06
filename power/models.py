from django.db import models

# Create your models here.

class PowerMeasurement(models.Model):
    UPS_STATUS_UNKNOWN = '1'
    UPS_STATUS_ONLINE = '2'
    UPS_STATUS_ONBATTERY = '3'
    UPS_STATUS_ONSMARTBOOST = '4'
    UPS_STATUS_TIMEDSLEEPING = '5'
    UPS_STATUS_SOFTWAREBYPASS = '6'
    UPS_STATUS_OFF = '7'
    UPS_STATUS_REBOOTING = '8'
    UPS_STATUS_SWITCHEDBYPASS = '9'
    UPS_STATUS_HARDWAREFAILUREBYPASS = '10'
    UPS_STATUS_SLEEPINGUNTILPOWERRETURN = '11'
    UPS_STATUS_ONSMARTTRIM = '12'
    
    UPS_STATUS_CHOICES = (
        (UPS_STATUS_UNKNOWN, 'Unknown'),
        (UPS_STATUS_ONLINE, 'Online'),
        (UPS_STATUS_ONBATTERY, 'Battery'),
        (UPS_STATUS_ONSMARTBOOST, 'Smart boost'),
        (UPS_STATUS_TIMEDSLEEPING, 'Timed sleeping'),
        (UPS_STATUS_SOFTWAREBYPASS, 'Software bypass'),
        (UPS_STATUS_OFF, 'Off'),
        (UPS_STATUS_REBOOTING, 'Rebooting'),
        (UPS_STATUS_SWITCHEDBYPASS, 'Switched bypass'),
        (UPS_STATUS_HARDWAREFAILUREBYPASS , 'Hardware failure bypass'),
        (UPS_STATUS_SLEEPINGUNTILPOWERRETURN , 'Sleeping until power returns'),
        (UPS_STATUS_ONSMARTTRIM, 'On smart trim')
    )

    time = models.DateTimeField()
    main_ups_status = models.CharField(max_length=2,
        choices=UPS_STATUS_CHOICES,
        default=UPS_STATUS_UNKNOWN)

    main_ups_battery = models.CharField(max_length=3, default=0)
    main_ups_load = models.CharField(max_length=3, default=0)

    dome_ups_status = models.CharField(max_length=2,
        choices=UPS_STATUS_CHOICES,
        default=UPS_STATUS_UNKNOWN)

    dome_ups_battery = models.CharField(max_length=3, default=0)
    dome_ups_load = models.CharField(max_length=3, default=0)

    roomalert_powered = models.BooleanField(default=True)

    pdu_nominal_computer = models.BooleanField(default=False)
    pdu_telescope_12v_power = models.BooleanField(default=False)
    pdu_telescope_80v_power = models.BooleanField(default=False)
    pdu_webcam_power = models.BooleanField(default=False)
    pdu_telescope_mixed_power = models.BooleanField(default=False)
    pdu_cover_motors = models.BooleanField(default=False)
    pdu_light = models.BooleanField(default=False)
    pdu_redundant_computer = models.BooleanField(default=False)
    pdu_dome_controler = models.BooleanField(default=False)
    pdu_dome_power = models.BooleanField(default=False)

    class Meta:
        get_latest_by = "time"
