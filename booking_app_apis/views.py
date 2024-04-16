from django.shortcuts import render
from .serializers import *
from bookingapp.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from bookingapp.flight_schedule import *
# Create your views here.

class FlightScheduleAPIView(APIView):
    serializer_class = FlightScheduleSerializer
    def post(self, request, *args, **kwargs):
        serializers = FlightScheduleSerializer(data=request.data)
        if serializers.is_valid():
            data = serializers.data
            print('data ',data)
            schedule_id = data.get('schedule_id')
            flight_number = data.get('flight_number')
            aircraft = data.get('aircraft')
            route = data.get('route')
            frequency = data.get('frequency')
            staff = data.get('staff')
            schedule_type = data.get('schedule_type')
            specific_date = data.get('specific_date')
            from_date = data.get('from_date')
            end_date = data.get('end_date')
            notes = data.get('notes')
            ticket_price = data.get('ticket_price')
            response =  flight_schedul(schedule_id, flight_number, aircraft, route, frequency, staff, 
                                       schedule_type, specific_date=specific_date,
                                       from_date=from_date, end_date=end_date, notes=notes, 
                                       ticket_price=ticket_price)
            print(response)
            return Response(data=serializers.data)
        else:
            print('seralizer error ', serializers.errors)
            return Response(data=serializers.errors)