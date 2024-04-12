from .models import *
from .convert_model_obj_to_dict import query_set_obj_to_dict,get_obj_to_dict
def displaying_flight_schedule_overview():
    try:        
        # Display an overview of existing flight schedules
        qs_obj = FlightSchedule.objects.all()
        excluded_column=['aircraft','staff','duration','distance','delay_reason','gate','notes','created_at','updated_at']
        if not qs_obj.exists():
            return qs_obj
        return query_set_obj_to_dict(qs_obj,excluded_column=excluded_column)
    except Exception as error:
        print('error ',error)
        return False
    
def edit_the_details_for_selected_flight(flight_number, **kwargs):
    try:        
        flight_schedule = FlightSchedule.objects.get(flight_number=flight_number)
        
        for field, value in kwargs.items():
            setattr(flight_schedule, field, value)
        
        flight_schedule.save()
        return 'success'
    except FlightSchedule.DoesNotExist:
        return False, "Flight schedule with the provided flight number does not exist"
    except Exception as error:
        print('error ',error)
        return False
    
def cancel_scheduled_flight(flight_number):
    '''
    This function is used to cancel the scheduled flight
    '''
    try:        
        flight_schedule = FlightSchedule.objects.get(flight_number=flight_number)
        status = flight_schedule.status
        if status == 'Cancelled':
            message='Flight already has been cancelled'
            return message
        if status != 'Scheduled':
            message='Can not perform cancellation request because flight not scheduled'
            return message
        if status == 'Scheduled':
            flight_schedule.status = 'Cancelled'
            flight_schedule.save()
            message='Flight cancelled'
            return message
    except FlightSchedule.DoesNotExist:
        return False, "Flight schedule with the provided flight number does not exist"
    except Exception as error:
        print('error ',error)
        return False
    
def add_new_flight_details(flight_number,airline,departure_airport,
                           arrival_airport,departure_time,arrival_time,
                           aircraft,total_seat,ticket_price
                           ):
    '''
    This function is used to add a new flight schedule
    '''
    try:
        # here default status will be scheduled
        FlightSchedule.objects.create(
            flight_number=flight_number,
            airline=airline,
            departure_airport=departure_airport,
            arrival_airport=arrival_airport,
            departure_time=departure_time,
            arrival_time=arrival_time,
            aircraft=aircraft,
            total_seat=total_seat,
            ticket_price=ticket_price,
            status='Scheduled'
        )
        return True
    except Exception as error:
        print('flight scheduling raising the error ',error)
        return error
def get_flight_for_confirm_cancellation(flight_number):
    try:
        get_obj = FlightSchedule.objects.get(flight_number=flight_number)
        excluded_column=['aircraft','staff','duration','distance','delay_reason','gate','notes','created_at','updated_at']
        return get_obj_to_dict(get_obj,excluded_column=excluded_column)
    except FlightSchedule.DoesNotExist:
        message = "records not found"
        return message
    except Exception as error:
        print('error ',error)
        return False
