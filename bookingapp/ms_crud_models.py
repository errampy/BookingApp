from .models import *
from django.utils.translation import gettext as _
from django.core.exceptions import ObjectDoesNotExist
def create_region(region_id, name):
    """
    Create a new region.
    """
    try:
        region = Region(region_id=region_id, name=name)
        region.save()
        return region
    except Exception as e:
        print(f"Error occurred while creating region: {e}")
        return None

def get_region(region_id):
    """
    Retrieve a region by its ID.
    """
    try:
        region = Region.objects.get(region_id=region_id)
        return region
    except Region.DoesNotExist:
        print(f"Region with ID {region_id} does not exist.")
        return None
    except Exception as e:
        print(f"Error occurred while retrieving region: {e}")
        return None

def update_region(region_id, name):
    """
    Update the details of an existing region.
    """
    region = get_region(region_id)
    if region:
        try:
            region.name = name
            region.save()
            return region
        except Exception as e:
            print(f"Error occurred while updating region: {e}")
            return None
    else:
        return None

def delete_region(region_id):
    """
    Delete a region by its ID.
    """
    region = get_region(region_id)
    if region:
        try:
            region.delete()
            return True
        except Exception as e:
            print(f"Error occurred while deleting region: {e}")
            return False
    else:
        return False

def create_airline(airline_id, name, code, logo, contact_person, email, phone_number, address):
    """
    Create a new airline.
    """
    try:
        airline = Airline(airline_id=airline_id, name=name, code=code, logo=logo, contact_person=contact_person, 
                          email=email, phone_number=phone_number, address=address)
        airline.save()
        return airline
    except Exception as e:
        print(f"Error occurred while creating airline: {e}")
        return None

def get_airline(airline_id):
    """
    Retrieve an airline by its ID.
    """
    try:
        airline = Airline.objects.get(airline_id=airline_id)
        return airline
    except Airline.DoesNotExist:
        print(f"Airline with ID {airline_id} does not exist.")
        return None
    except Exception as e:
        print(f"Error occurred while retrieving airline: {e}")
        return None

def update_airline(airline_id, name, code, logo, contact_person, email, phone_number, address):
    """
    Update the details of an existing airline.
    """
    airline = get_airline(airline_id)
    if airline:
        try:
            airline.name = name
            airline.code = code
            airline.logo = logo
            airline.contact_person = contact_person
            airline.email = email
            airline.phone_number = phone_number
            airline.address = address
            airline.save()
            return airline
        except Exception as e:
            print(f"Error occurred while updating airline: {e}")
            return None
    else:
        return None

def delete_airline(airline_id):
    """
    Delete an airline by its ID.
    """
    airline = get_airline(airline_id)
    if airline:
        try:
            airline.delete()
            return True
        except Exception as e:
            print(f"Error occurred while deleting airline: {e}")
            return False
    else:
        return False

def create_engine_type(type_id, type_name, description=None):
    try:
        engine_type = EngineType.objects.create(
            type_id=type_id,
            type_name=type_name,
            description=description
        )
        return engine_type
    except Exception as e:
        print(f"Error occurred while creating engine type: {e}")
        return None

def get_engine_type(type_id):
    try:
        engine_type = EngineType.objects.get(type_id=type_id)
        return engine_type
    except EngineType.DoesNotExist:
        print(f"Engine type with ID {type_id} does not exist.")
        return None
    except Exception as e:
        print(f"Error occurred while retrieving engine type: {e}")
        return None

def update_engine_type(type_id, type_name=None, description=None):
    engine_type = get_engine_type(type_id)
    if engine_type:
        try:
            if type_name:
                engine_type.type_name = type_name
            if description is not None:
                engine_type.description = description
            engine_type.save()
            return engine_type
        except Exception as e:
            print(f"Error occurred while updating engine type: {e}")
            return None
    else:
        print(f"Engine type with ID {type_id} does not exist.")
        return None

def delete_engine_type(type_id):
    engine_type = get_engine_type(type_id)
    if engine_type:
        try:
            engine_type.delete()
            return True
        except Exception as e:
            print(f"Error occurred while deleting engine type: {e}")
            return False
    else:
        print(f"Engine type with ID {type_id} does not exist.")
        return False

def create_aircraft_type(type_id, type_name):
    try:
        aircraft_type = AircraftType.objects.create(
            type_id=type_id,
            type_name=type_name
        )
        return aircraft_type
    except Exception as e:
        print(f"Error occurred while creating aircraft type: {e}")
        return None

def get_aircraft_type(type_id):
    try:
        aircraft_type = AircraftType.objects.get(type_id=type_id)
        return aircraft_type
    except AircraftType.DoesNotExist:
        print(f"Aircraft type with ID {type_id} does not exist.")
        return None
    except Exception as e:
        print(f"Error occurred while retrieving aircraft type: {e}")
        return None

def update_aircraft_type(type_id, type_name):
    aircraft_type = get_aircraft_type(type_id)
    if aircraft_type:
        try:
            aircraft_type.type_name = type_name
            aircraft_type.save()
            return aircraft_type
        except Exception as e:
            print(f"Error occurred while updating aircraft type: {e}")
            return None
    else:
        print(f"Aircraft type with ID {type_id} does not exist.")
        return None

def delete_aircraft_type(type_id):
    aircraft_type = get_aircraft_type(type_id)
    if aircraft_type:
        try:
            aircraft_type.delete()
            return True
        except Exception as e:
            print(f"Error occurred while deleting aircraft type: {e}")
            return False
    else:
        print(f"Aircraft type with ID {type_id} does not exist.")
        return False

def create_aircraft_status_type(type_id, type_name):
    try:
        aircraft_status_type = AircraftStatusType.objects.create(
            type_id=type_id,
            type_name=type_name
        )
        return aircraft_status_type
    except Exception as e:
        print(f"Error occurred while creating aircraft status type: {e}")
        return None

def get_aircraft_status_type(type_id):
    try:
        aircraft_status_type = AircraftStatusType.objects.get(type_id=type_id)
        return aircraft_status_type
    except AircraftStatusType.DoesNotExist:
        print(f"Aircraft status type with ID {type_id} does not exist.")
        return None
    except Exception as e:
        print(f"Error occurred while retrieving aircraft status type: {e}")
        return None

def update_aircraft_status_type(type_id, type_name):
    aircraft_status_type = get_aircraft_status_type(type_id)
    if aircraft_status_type:
        try:
            aircraft_status_type.type_name = type_name
            aircraft_status_type.save()
            return aircraft_status_type
        except Exception as e:
            print(f"Error occurred while updating aircraft status type: {e}")
            return None
    else:
        print(f"Aircraft status type with ID {type_id} does not exist.")
        return None

def delete_aircraft_status_type(type_id):
    aircraft_status_type = get_aircraft_status_type(type_id)
    if aircraft_status_type:
        try:
            aircraft_status_type.delete()
            return True
        except Exception as e:
            print(f"Error occurred while deleting aircraft status type: {e}")
            return False
    else:
        print(f"Aircraft status type with ID {type_id} does not exist.")
        return False

def create_aircraft(aircraft_id, airline, model_name, aircraft_type, manufacturer, registration_number,
                    seating_capacity, maximum_speed, maximum_range, manufacture_date, last_maintenance_date,
                    engine_type, engines_count, current_status, first_class_seats=None, business_class_seats=None,
                    economy_class_seats=None):
    try:
        aircraft = Aircraft.objects.create(
            aircraft_id=aircraft_id,
            airline=airline,
            model_name=model_name,
            aircraft_type=aircraft_type,
            manufacturer=manufacturer,
            registration_number=registration_number,
            seating_capacity=seating_capacity,
            maximum_speed=maximum_speed,
            maximum_range=maximum_range,
            manufacture_date=manufacture_date,
            last_maintenance_date=last_maintenance_date,
            engine_type=engine_type,
            engines_count=engines_count,
            first_class_seats=first_class_seats,
            business_class_seats=business_class_seats,
            economy_class_seats=economy_class_seats,
            current_status=current_status
        )
        return aircraft
    except Exception as e:
        print(f"Error occurred while creating aircraft: {e}")
        return None

def get_aircraft(aircraft_id):
    try:
        aircraft = Aircraft.objects.get(aircraft_id=aircraft_id)
        return aircraft
    except Aircraft.DoesNotExist:
        print(f"Aircraft with ID {aircraft_id} does not exist.")
        return None
    except Exception as e:
        print(f"Error occurred while retrieving aircraft: {e}")
        return None

def update_aircraft(aircraft_id, **kwargs):
    aircraft = get_aircraft(aircraft_id)
    if aircraft:
        for key, value in kwargs.items():
            setattr(aircraft, key, value)
        try:
            aircraft.save()
            return aircraft
        except Exception as e:
            print(f"Error occurred while updating aircraft: {e}")
            return None
    else:
        print(f"Aircraft with ID {aircraft_id} does not exist.")
        return None

def delete_aircraft(aircraft_id):
    aircraft = get_aircraft(aircraft_id)
    if aircraft:
        try:
            aircraft.delete()
            return True
        except Exception as e:
            print(f"Error occurred while deleting aircraft: {e}")
            return False
    else:
        print(f"Aircraft with ID {aircraft_id} does not exist.")
        return False

def create_staff_position_type(sp_type_id, position_type):
    try:
        staff_position_type = StaffPositionType.objects.create(
            sp_type_id=sp_type_id,
            position_type=position_type
        )
        return staff_position_type
    except Exception as e:
        print(f"Error occurred while creating staff position type: {e}")
        return None

def get_staff_position_type(sp_type_id):
    try:
        staff_position_type = StaffPositionType.objects.get(sp_type_id=sp_type_id)
        return staff_position_type
    except StaffPositionType.DoesNotExist:
        print(f"Staff position type with ID {sp_type_id} does not exist.")
        return None
    except Exception as e:
        print(f"Error occurred while retrieving staff position type: {e}")
        return None

def update_staff_position_type(sp_type_id, position_type):
    staff_position_type = get_staff_position_type(sp_type_id)
    if staff_position_type:
        staff_position_type.position_type = position_type
        try:
            staff_position_type.save()
            return staff_position_type
        except Exception as e:
            print(f"Error occurred while updating staff position type: {e}")
            return None
    else:
        print(f"Staff position type with ID {sp_type_id} does not exist.")
        return None

def delete_staff_position_type(sp_type_id):
    staff_position_type = get_staff_position_type(sp_type_id)
    if staff_position_type:
        try:
            staff_position_type.delete()
            return True
        except Exception as e:
            print(f"Error occurred while deleting staff position type: {e}")
            return False
    else:
        print(f"Staff position type with ID {sp_type_id} does not exist.")
        return False

def create_staff(staff_id, user_id, position_id, airline_id):
    try:
        user = User.objects.get(id=user_id)
        position = StaffPositionType.objects.get(sp_type_id=position_id)
        airline = Airline.objects.get(airline_id=airline_id)
        staff = Staff.objects.create(
            staff_id=staff_id,
            user=user,
            position=position,
            airline=airline
        )
        return staff
    except ObjectDoesNotExist as e:
        print(f"Error occurred while creating staff: {e}")
        return None
    except Exception as e:
        print(f"Error occurred while creating staff: {e}")
        return None

def get_staff(staff_id):
    try:
        staff = Staff.objects.get(staff_id=staff_id)
        return staff
    except Staff.DoesNotExist:
        print(f"Staff with ID {staff_id} does not exist.")
        return None
    except Exception as e:
        print(f"Error occurred while retrieving staff: {e}")
        return None

def update_staff(staff_id, user_id=None, position_id=None, airline_id=None):
    staff = get_staff(staff_id)
    if staff:
        try:
            if user_id:
                staff.user = User.objects.get(id=user_id)
            if position_id:
                staff.position = StaffPositionType.objects.get(sp_type_id=position_id)
            if airline_id:
                staff.airline = Airline.objects.get(airline_id=airline_id)
            staff.save()
            return staff
        except ObjectDoesNotExist as e:
            print(f"Error occurred while updating staff: {e}")
            return None
        except Exception as e:
            print(f"Error occurred while updating staff: {e}")
            return None
    else:
        print(f"Staff with ID {staff_id} does not exist.")
        return None

def delete_staff(staff_id):
    staff = get_staff(staff_id)
    if staff:
        try:
            staff.delete()
            return True
        except Exception as e:
            print(f"Error occurred while deleting staff: {e}")
            return False
    else:
        print(f"Staff with ID {staff_id} does not exist.")
        return False

def create_airport(code, name, country_id, county_or_state_id, city_id, latitude, longitude):
    try:
        country = Country.objects.get(id=country_id)
        county_or_state = CountyOrState.objects.get(id=county_or_state_id)
        city = City.objects.get(id=city_id)
        airport = Airport.objects.create(
            code=code,
            name=name,
            country=country,
            county_or_state=county_or_state,
            city=city,
            latitude=latitude,
            longitude=longitude
        )
        return airport
    except ObjectDoesNotExist as e:
        print(f"Error occurred while creating airport: {e}")
        return None
    except Exception as e:
        print(f"Error occurred while creating airport: {e}")
        return None

def get_airport(airport_id):
    try:
        airport = Airport.objects.get(airport_id=airport_id)
        return airport
    except Airport.DoesNotExist:
        print(f"Airport with ID {airport_id} does not exist.")
        return None
    except Exception as e:
        print(f"Error occurred while retrieving airport: {e}")
        return None

def update_airport(airport_id, code=None, name=None, country_id=None, county_or_state_id=None, city_id=None, latitude=None, longitude=None):
    airport = get_airport(airport_id)
    if airport:
        try:
            if code:
                airport.code = code
            if name:
                airport.name = name
            if country_id:
                airport.country = Country.objects.get(id=country_id)
            if county_or_state_id:
                airport.county_or_state = CountyOrState.objects.get(id=county_or_state_id)
            if city_id:
                airport.city = City.objects.get(id=city_id)
            if latitude:
                airport.latitude = latitude
            if longitude:
                airport.longitude = longitude
            airport.save()
            return airport
        except ObjectDoesNotExist as e:
            print(f"Error occurred while updating airport: {e}")
            return None
        except Exception as e:
            print(f"Error occurred while updating airport: {e}")
            return None
    else:
        print(f"Airport with ID {airport_id} does not exist.")
        return None

def delete_airport(airport_id):
    airport = get_airport(airport_id)
    if airport:
        try:
            airport.delete()
            return True
        except Exception as e:
            print(f"Error occurred while deleting airport: {e}")
            return False
    else:
        print(f"Airport with ID {airport_id} does not exist.")
        return False

def create_flight_registration(flight_number, airline_id):
    try:
        airline = Airline.objects.get(airline_id=airline_id)
        flight_registration = FlightRegistration.objects.create(
            flight_number=flight_number,
            airline=airline
        )
        return flight_registration
    except ObjectDoesNotExist as e:
        print(f"Error occurred while creating flight registration: {e}")
        return None
    except Exception as e:
        print(f"Error occurred while creating flight registration: {e}")
        return None

def get_flight_registration(flight_number):
    try:
        flight_registration = FlightRegistration.objects.get(flight_number=flight_number)
        return flight_registration
    except FlightRegistration.DoesNotExist:
        print(f"Flight registration with flight number {flight_number} does not exist.")
        return None
    except Exception as e:
        print(f"Error occurred while retrieving flight registration: {e}")
        return None

def update_flight_registration(flight_number, airline_id=None):
    flight_registration = get_flight_registration(flight_number)
    if flight_registration:
        try:
            if airline_id:
                flight_registration.airline = Airline.objects.get(airline_id=airline_id)
            flight_registration.save()
            return flight_registration
        except ObjectDoesNotExist as e:
            print(f"Error occurred while updating flight registration: {e}")
            return None
        except Exception as e:
            print(f"Error occurred while updating flight registration: {e}")
            return None
    else:
        print(f"Flight registration with flight number {flight_number} does not exist.")
        return None

def delete_flight_registration(flight_number):
    flight_registration = get_flight_registration(flight_number)
    if flight_registration:
        try:
            flight_registration.delete()
            return True
        except Exception as e:
            print(f"Error occurred while deleting flight registration: {e}")
            return False
    else:
        print(f"Flight registration with flight number {flight_number} does not exist.")
        return False

def create_flight_schedule(schedule_id, flight_number, airline_id, departure_airport_id, arrival_airport_id, departure_time, arrival_time, aircraft_id, status, duration=None, distance=None, delay_reason=None, gate=None, notes=None, total_seat=30, ticket_price=None):
    try:
        airline = Airline.objects.get(airline_id=airline_id)
        departure_airport = Airport.objects.get(airport_id=departure_airport_id)
        arrival_airport = Airport.objects.get(airport_id=arrival_airport_id)
        aircraft = Aircraft.objects.get(aircraft_id=aircraft_id)
        
        flight_schedule = FlightSchedule.objects.create(
            schedule_id=schedule_id,
            flight_number=flight_number,
            airline=airline,
            departure_airport=departure_airport,
            arrival_airport=arrival_airport,
            departure_time=departure_time,
            arrival_time=arrival_time,
            aircraft=aircraft,
            status=status,
            duration=duration,
            distance=distance,
            delay_reason=delay_reason,
            gate=gate,
            notes=notes,
            total_seat=total_seat,
            ticket_price=ticket_price
        )
        return flight_schedule
    except ObjectDoesNotExist as e:
        print(f"Error occurred while creating flight schedule: {e}")
        return None
    except Exception as e:
        print(f"Error occurred while creating flight schedule: {e}")
        return None

def get_flight_schedule(schedule_id):
    try:
        flight_schedule = FlightSchedule.objects.get(schedule_id=schedule_id)
        return flight_schedule
    except FlightSchedule.DoesNotExist:
        print(f"Flight schedule with schedule ID {schedule_id} does not exist.")
        return None
    except Exception as e:
        print(f"Error occurred while retrieving flight schedule: {e}")
        return None

def update_flight_schedule(schedule_id, **kwargs):
    flight_schedule = get_flight_schedule(schedule_id)
    if flight_schedule:
        try:
            for key, value in kwargs.items():
                setattr(flight_schedule, key, value)
            flight_schedule.save()
            return flight_schedule
        except ObjectDoesNotExist as e:
            print(f"Error occurred while updating flight schedule: {e}")
            return None
        except Exception as e:
            print(f"Error occurred while updating flight schedule: {e}")
            return None
    else:
        print(f"Flight schedule with schedule ID {schedule_id} does not exist.")
        return None

def delete_flight_schedule(schedule_id):
    flight_schedule = get_flight_schedule(schedule_id)
    if flight_schedule:
        try:
            flight_schedule.delete()
            return True
        except Exception as e:
            print(f"Error occurred while deleting flight schedule: {e}")
            return False
    else:
        print(f"Flight schedule with schedule ID {schedule_id} does not exist.")
        return False

def create_distance_type(type_name):
    try:
        distance_type = DistanceType.objects.create(type_name=type_name)
        return distance_type
    except Exception as e:
        print(f"Error occurred while creating distance type: {e}")
        return None

def get_distance_type(type_id):
    try:
        distance_type = DistanceType.objects.get(pk=type_id)
        return distance_type
    except DistanceType.DoesNotExist:
        print(f"Distance type with ID {type_id} does not exist.")
        return None
    except Exception as e:
        print(f"Error occurred while retrieving distance type: {e}")
        return None

def update_distance_type(type_id, type_name):
    distance_type = get_distance_type(type_id)
    if distance_type:
        try:
            distance_type.type_name = type_name
            distance_type.save()
            return distance_type
        except Exception as e:
            print(f"Error occurred while updating distance type: {e}")
            return None
    else:
        print(f"Distance type with ID {type_id} does not exist.")
        return None

def delete_distance_type(type_id):
    distance_type = get_distance_type(type_id)
    if distance_type:
        try:
            distance_type.delete()
            return True
        except Exception as e:
            print(f"Error occurred while deleting distance type: {e}")
            return False
    else:
        print(f"Distance type with ID {type_id} does not exist.")
        return False

def create_route(route_id, departure_airport, arrival_airport, distance_type, distance_value, estimated_flight_time, route_status):
    try:
        route = Routes.objects.create(
            route_id=route_id,
            departure_airport=departure_airport,
            arrival_airport=arrival_airport,
            distance_type=distance_type,
            distance_value=distance_value,
            estimated_flight_time=estimated_flight_time,
            route_status=route_status
        )
        return route
    except Exception as e:
        print(f"Error occurred while creating route: {e}")
        return None

def get_route(route_id):
    try:
        route = Routes.objects.get(pk=route_id)
        return route
    except Routes.DoesNotExist:
        print(f"Route with ID {route_id} does not exist.")
        return None
    except Exception as e:
        print(f"Error occurred while retrieving route: {e}")
        return None

def update_route(route_id, departure_airport, arrival_airport, distance_type, distance_value, estimated_flight_time, route_status):
    route = get_route(route_id)
    if route:
        try:
            route.departure_airport = departure_airport
            route.arrival_airport = arrival_airport
            route.distance_type = distance_type
            route.distance_value = distance_value
            route.estimated_flight_time = estimated_flight_time
            route.route_status = route_status
            route.save()
            return route
        except Exception as e:
            print(f"Error occurred while updating route: {e}")
            return None
    else:
        print(f"Route with ID {route_id} does not exist.")
        return None

def delete_route(route_id):
    route = get_route(route_id)
    if route:
        try:
            route.delete()
            return True
        except Exception as e:
            print(f"Error occurred while deleting route: {e}")
            return False
    else:
        print(f"Route with ID {route_id} does not exist.")
        return False

def create_day_of_operation(day_name):
    try:
        day_of_operation = DayOfOperation.objects.create(day_name=day_name)
        return day_of_operation
    except Exception as e:
        print(f"Error occurred while creating day of operation: {e}")
        return None

def get_day_of_operation(day_id):
    try:
        day_of_operation = DayOfOperation.objects.get(pk=day_id)
        return day_of_operation
    except DayOfOperation.DoesNotExist:
        print(f"Day of operation with ID {day_id} does not exist.")
        return None
    except Exception as e:
        print(f"Error occurred while retrieving day of operation: {e}")
        return None

def update_day_of_operation(day_id, day_name):
    day_of_operation = get_day_of_operation(day_id)
    if day_of_operation:
        try:
            day_of_operation.day_name = day_name
            day_of_operation.save()
            return day_of_operation
        except Exception as e:
            print(f"Error occurred while updating day of operation: {e}")
            return None
    else:
        print(f"Day of operation with ID {day_id} does not exist.")
        return None

def delete_day_of_operation(day_id):
    day_of_operation = get_day_of_operation(day_id)
    if day_of_operation:
        try:
            day_of_operation.delete()
            return True
        except Exception as e:
            print(f"Error occurred while deleting day of operation: {e}")
            return False
    else:
        print(f"Day of operation with ID {day_id} does not exist.")
        return False

def create_flight_frequency(route, departure_time, arrival_time, days_of_operation, aircraft_type_id, flight_status):
    try:
        flight_frequency = FlightFrequencies.objects.create(
            route=route,
            departure_time=departure_time,
            arrival_time=arrival_time,
            days_of_operation=days_of_operation,
            aircraft_type_id=aircraft_type_id,
            flight_status=flight_status
        )
        return flight_frequency
    except Exception as e:
        print(f"Error occurred while creating flight frequency: {e}")
        return None

def get_flight_frequency(frequency_id):
    try:
        flight_frequency = FlightFrequencies.objects.get(pk=frequency_id)
        return flight_frequency
    except FlightFrequencies.DoesNotExist:
        print(f"Flight frequency with ID {frequency_id} does not exist.")
        return None
    except Exception as e:
        print(f"Error occurred while retrieving flight frequency: {e}")
        return None

def update_flight_frequency(frequency_id, route, departure_time, arrival_time, days_of_operation, aircraft_type_id, flight_status):
    flight_frequency = get_flight_frequency(frequency_id)
    if flight_frequency:
        try:
            flight_frequency.route = route
            flight_frequency.departure_time = departure_time
            flight_frequency.arrival_time = arrival_time
            flight_frequency.days_of_operation = days_of_operation
            flight_frequency.aircraft_type_id = aircraft_type_id
            flight_frequency.flight_status = flight_status
            flight_frequency.save()
            return flight_frequency
        except Exception as e:
            print(f"Error occurred while updating flight frequency: {e}")
            return None
    else:
        print(f"Flight frequency with ID {frequency_id} does not exist.")
        return None

def delete_flight_frequency(frequency_id):
    flight_frequency = get_flight_frequency(frequency_id)
    if flight_frequency:
        try:
            flight_frequency.delete()
            return True
        except Exception as e:
            print(f"Error occurred while deleting flight frequency: {e}")
            return False
    else:
        print(f"Flight frequency with ID {frequency_id} does not exist.")
        return False
def create_crew_type(type_name, description=None):
    try:
        crew_type = CrewType.objects.create(
            type_name=type_name,
            description=description
        )
        return crew_type
    except Exception as e:
        print(f"Error occurred while creating crew type: {e}")
        return None

def get_crew_type(type_id):
    try:
        crew_type = CrewType.objects.get(pk=type_id)
        return crew_type
    except CrewType.DoesNotExist:
        print(f"Crew type with ID {type_id} does not exist.")
        return None
    except Exception as e:
        print(f"Error occurred while retrieving crew type: {e}")
        return None

def update_crew_type(type_id, type_name, description=None):
    crew_type = get_crew_type(type_id)
    if crew_type:
        try:
            crew_type.type_name = type_name
            crew_type.description = description
            crew_type.save()
            return crew_type
        except Exception as e:
            print(f"Error occurred while updating crew type: {e}")
            return None
    else:
        print(f"Crew type with ID {type_id} does not exist.")
        return None

def delete_crew_type(type_id):
    crew_type = get_crew_type(type_id)
    if crew_type:
        try:
            crew_type.delete()
            return True
        except Exception as e:
            print(f"Error occurred while deleting crew type: {e}")
            return False
    else:
        print(f"Crew type with ID {type_id} does not exist.")
        return False
def create_crew_active_status(status_name):
    try:
        crew_active_status = CrewActiveStatus.objects.create(
            status_name=status_name,
        )
        return crew_active_status
    except Exception as e:
        print(f"Error occurred while creating crew active status: {e}")
        return None

def get_crew_active_status(status_id):
    try:
        crew_active_status = CrewActiveStatus.objects.get(pk=status_id)
        return crew_active_status
    except CrewActiveStatus.DoesNotExist:
        print(f"Crew active status with ID {status_id} does not exist.")
        return None
    except Exception as e:
        print(f"Error occurred while retrieving crew active status: {e}")
        return None

def update_crew_active_status(status_id, status_name):
    crew_active_status = get_crew_active_status(status_id)
    if crew_active_status:
        try:
            crew_active_status.status_name = status_name
            crew_active_status.save()
            return crew_active_status
        except Exception as e:
            print(f"Error occurred while updating crew active status: {e}")
            return None
    else:
        print(f"Crew active status with ID {status_id} does not exist.")
        return None

def delete_crew_active_status(status_id):
    crew_active_status = get_crew_active_status(status_id)
    if crew_active_status:
        try:
            crew_active_status.delete()
            return True
        except Exception as e:
            print(f"Error occurred while deleting crew active status: {e}")
            return False
    else:
        print(f"Crew active status with ID {status_id} does not exist.")
        return False

def create_crew(crew_type, crew_name, license_certification_info, license_certification_id, license_certification_name, license_certification_valid_upto, base_location, phone_number, email, active_status):
    try:
        crew = Crew.objects.create(
            crew_type=crew_type,
            crew_name=crew_name,
            license_certification_info=license_certification_info,
            license_certification_id=license_certification_id,
            license_certification_name=license_certification_name,
            license_certification_valid_upto=license_certification_valid_upto,
            base_location=base_location,
            phone_number=phone_number,
            email=email,
            active_status=active_status,
        )
        return crew
    except Exception as e:
        print(f"Error occurred while creating crew: {e}")
        return None

def get_crew(crew_id):
    try:
        crew = Crew.objects.get(pk=crew_id)
        return crew
    except Crew.DoesNotExist:
        print(f"Crew with ID {crew_id} does not exist.")
        return None
    except Exception as e:
        print(f"Error occurred while retrieving crew: {e}")
        return None

def update_crew(crew_id, crew_type, crew_name, license_certification_info, license_certification_id, license_certification_name, license_certification_valid_upto, base_location, phone_number, email, active_status):
    crew = get_crew(crew_id)
    if crew:
        try:
            crew.crew_type = crew_type
            crew.crew_name = crew_name
            crew.license_certification_info = license_certification_info
            crew.license_certification_id = license_certification_id
            crew.license_certification_name = license_certification_name
            crew.license_certification_valid_upto = license_certification_valid_upto
            crew.base_location = base_location
            crew.phone_number = phone_number
            crew.email = email
            crew.active_status = active_status
            crew.save()
            return crew
        except Exception as e:
            print(f"Error occurred while updating crew: {e}")
            return None
    else:
        print(f"Crew with ID {crew_id} does not exist.")
        return None

def delete_crew(crew_id):
    crew = get_crew(crew_id)
    if crew:
        try:
            crew.delete()
            return True
        except Exception as e:
            print(f"Error occurred while deleting crew: {e}")
            return False
    else:
        print(f"Crew with ID {crew_id} does not exist.")
        return False

def create_flight_requirement(route_id, aircraft_type_id, minimum_crew_members, maximum_cargo_weight, special_equipment_needed, additional_considerations):
    try:
        flight_requirement = FlightRequirements.objects.create(
            route_id=route_id,
            aircraft_type_id=aircraft_type_id,
            minimum_crew_members=minimum_crew_members,
            maximum_cargo_weight=maximum_cargo_weight,
            special_equipment_needed=special_equipment_needed,
            additional_considerations=additional_considerations,
        )
        return flight_requirement
    except Exception as e:
        print(f"Error occurred while creating flight requirement: {e}")
        return None

def get_flight_requirement(requirement_id):
    try:
        flight_requirement = FlightRequirements.objects.get(pk=requirement_id)
        return flight_requirement
    except FlightRequirements.DoesNotExist:
        print(f"Flight requirement with ID {requirement_id} does not exist.")
        return None
    except Exception as e:
        print(f"Error occurred while retrieving flight requirement: {e}")
        return None

def update_flight_requirement(requirement_id, route_id, aircraft_type_id, minimum_crew_members, maximum_cargo_weight, special_equipment_needed, additional_considerations):
    flight_requirement = get_flight_requirement(requirement_id)
    if flight_requirement:
        try:
            flight_requirement.route_id = route_id
            flight_requirement.aircraft_type_id = aircraft_type_id
            flight_requirement.minimum_crew_members = minimum_crew_members
            flight_requirement.maximum_cargo_weight = maximum_cargo_weight
            flight_requirement.special_equipment_needed = special_equipment_needed
            flight_requirement.additional_considerations = additional_considerations
            flight_requirement.save()
            return flight_requirement
        except Exception as e:
            print(f"Error occurred while updating flight requirement: {e}")
            return None
    else:
        print(f"Flight requirement with ID {requirement_id} does not exist.")
        return None

def delete_flight_requirement(requirement_id):
    flight_requirement = get_flight_requirement(requirement_id)
    if flight_requirement:
        try:
            flight_requirement.delete()
            return True
        except Exception as e:
            print(f"Error occurred while deleting flight requirement: {e}")
            return False
    else:
        print(f"Flight requirement with ID {requirement_id} does not exist.")
        return False
