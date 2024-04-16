from .convert_model_obj_to_dict import get_obj_to_dict, query_set_obj_to_dict
from .models import *
from bookingpro.response_template import response_template
from django.db.models import Q
from datetime import datetime, timedelta
from bookingapp.ms_crud_models import *




def generate_schedule(start_date, end_date, operation_days):
    # Convert start_date and end_date strings to datetime objects
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    
    # Initialize list to store the scheduled dates
    scheduled_dates = []
    
    # Iterate through the date range
    current_date = start_date
    while current_date <= end_date:
        # Check if the current day is in the operation days list
        if current_date.strftime('%A') in operation_days:
            scheduled_dates.append(current_date.strftime('%Y-%m-%d'))
        
        # Move to the next day
        current_date += timedelta(days=1)
    print('scheduled_dates ',scheduled_dates)
    
    return scheduled_dates

def check_date_given_or_not(specific_date,from_date,end_date):
    if specific_date is None and from_date is None and end_date is None:
        return response_template(False,"Must be any one from this 'specific_date', 'from_date' and 'end_date' ")
    else:
        return response_template(True)
def check_required_fields_againest_schedule_type(schedule_type, specific_date=None, from_date=None, end_date=None):
    if schedule_type == 'specific_date':
        if specific_date is None:
            return response_template(False,"specific_date should not be empty")
        else:
            return response_template(True)
    elif schedule_type == 'date_range':
        if from_date is None and end_date is None:
            return response_template(False,"from_date and end_date should not be empty if selected 'date range' ")
        else:
            return response_template(True)
    else:
        return response_template(False,"Invalid schedule_type must be any one from these 'specific_date' or 'date_range' ")

def check_aircraft(aircraft_id):
    '''
    Function Name : check_aircraft
    Argument : aircraft_id

    Desc : It is responsible to check provided aircraft id is exists or not, if exists then return the True and aircraft details else False and Invalid aircraft id

    '''
    try:
        get_obj = Aircraft.objects.get(aircraft_id=aircraft_id)
        return response_template(True,get_obj_to_dict(get_obj))
    except Aircraft.DoesNotExist:
        return response_template(False, "Invalid aircraft Id")
def check_route(route_id):
    '''
    Function Name : check_route
    Argument : route_id

    Desc : It is responsible to check provided route id is exists or not, if exists then return the True and route details else False and Invalid route id

    '''
    try:
        get_obj = Routes.objects.get(route_id=route_id)
        return response_template(True,get_obj_to_dict(get_obj))
    except Routes.DoesNotExist:
        return response_template(False, "Invalid route Id")
def check_frequency(frequency_id):
    '''
    Function Name : check_frequency
    Argument : frequency_id

    Desc : It is responsible to check provided frequency id is exists or not, if exists then return the True and frequency details else False and Invalid frequency id

    '''
    try:
        get_obj = FlightFrequencies.objects.get(frequency_id=frequency_id)
        return response_template(True,get_obj_to_dict(get_obj))
    except FlightFrequencies.DoesNotExist:
        return response_template(False, "Invalid route Id")
def check_frequency_and_valid_mapped_or_not(frequency_id,route_id):
    '''
    Function Name : check_frequency_and_valid_mapped_or_not
    Argument : frequency_id,route_id

    Desc : It is responsible to check provided frequency id  and route_id both are already mapped or not , if its satishfiled then return True else False
    '''
    try:
        qs_obj = FlightFrequencies.objects.filter(Q(frequency_id=frequency_id)&Q(route_id=route_id))
        if qs_obj.exists():
            return response_template(True)
        else:
            return response_template(False)
    except Exception as error:
        return response_template(False, f'''{error}''')

def flight_schedul(schedule_id, flight_number, aircraft, route, frequency, staff, schedule_type, status, specific_date=None, from_date=None, end_date=None, notes=None, ticket_price=None):
    response = check_date_given_or_not(specific_date,from_date,end_date)
    print(response)
    if not response.get('status'):
        return response
    response = check_required_fields_againest_schedule_type(schedule_type, specific_date, from_date, end_date)
    if not response.get('status'):
        return response
    response = check_aircraft(aircraft)
    if not response.get('status'):
        return response
    response = check_route(route)
    if not response.get('status'):
        return response
    response = check_frequency(frequency)
    if not response.get('status'):
        return response
    response = check_frequency_and_valid_mapped_or_not(frequency, route)
    if not response.get('status'):
        return response
    response = create_flight_schedule(schedule_id, flight_number, aircraft, route, frequency, 
                           staff, schedule_type, status,specific_date=specific_date, 
                           from_date=from_date, end_date=end_date, notes=notes, 
                           ticket_price=ticket_price)
    
    # this is in processing .......
    return 'success'

    
    