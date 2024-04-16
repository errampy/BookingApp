from rest_framework import serializers
from bookingapp.models import *

class FlightScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightSchedule
        fields = '__all__'