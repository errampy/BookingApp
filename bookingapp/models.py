from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from .models_master_general import *

class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        return self.create_user(email, password, **other_fields)

    def create_user(self, email, password, **other_fields):
        if not email:
            raise ValueError(_("You must provide a valid email address"))

        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100, blank=False, null=True)
    last_name = models.CharField(max_length=100, blank=False, null=True)
    email = models.EmailField(_("email address"), unique=True)
    phone_no = models.CharField(max_length=15, blank=False, null=False)
    nationality = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    objects = CustomUserManager()

    REQUIRED_FIELDS = ["phone_no", "nationality",]

    USERNAME_FIELD = "email"

    def __str__(self):
        return str(self.email)
#  this models for MS

class MSRegistration(models.Model):
    mservice_id = models.CharField(max_length=20,primary_key=True)
    mservice_name = models.CharField(max_length=100)
    arguments = models.JSONField(null=True,blank=True)
    arguments_list = models.TextField(null=True,blank=True)
    required_parameter = models.TextField(null=True,blank=True)
    optional_parameter = models.TextField(null=True,blank=True)
    is_authenticate = models.BooleanField(default=False)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.mservice_name)
    
class ModuleRegistration(models.Model):
    module_name = models.CharField(max_length=250,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def str(self):
        return str(self.module_name)

class MsToModuleMapping(models.Model):
    mservice_id = models.OneToOneField(MSRegistration,on_delete=models.CASCADE,related_name='ms_id')
    module_id = models.ForeignKey(ModuleRegistration,on_delete=models.CASCADE,related_name='module_id')

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def str(self):
        return str(self.module_id)	

class Region(models.Model):
    """
    Model representing a geographic region.
    """
    region_id = models.CharField(max_length=100, primary_key=True, help_text="Id of the region")  # Id of the region
    name = models.CharField(max_length=100, unique=True, help_text="Name of the region")  # Name of the region
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time of creation")  # Date and time of creation
    updated_at = models.DateTimeField(auto_now=True, help_text="Date and time of last update")      # Date and time of last update

    def __str__(self):
        return self.name

class Airline(models.Model):
    """
    Model representing an airline company.
    """
    airline_id = models.CharField(max_length=100, primary_key=True, help_text="Id of the airline")    # Id of the airline
    name = models.CharField(max_length=100, unique=True, help_text="Name of the airline")                      # Name of the airline
    code = models.CharField(max_length=3, unique=True, help_text="Code of the airline")            # Code of the airline
    logo = models.ImageField(upload_to='airline_logos/', null=True, blank=True, help_text="Logo of the airline")  # Logo of the airline
    contact_person = models.CharField(max_length=100, help_text="Contact person of the airline")   # Contact person of the airline
    email = models.EmailField(help_text="Email of the airline")                                    # Email of the airline
    phone_number = models.CharField(max_length=20, help_text="Phone number of the airline")        # Phone number of the airline
    address = models.TextField(help_text="Address of the airline")                                 # Address of the airline
    operating_regions = models.ManyToManyField(Region, help_text="Regions where the airline operates")  # Regions where the airline operates
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time of creation")    # Date and time of creation
    updated_at = models.DateTimeField(auto_now=True, help_text="Date and time of last update")      # Date and time of last update

    def __str__(self):
        return self.airline_id

class EngineType(models.Model):
    """
    Model representing an engine type.
    """
    type_id = models.CharField(max_length=20, primary_key=True, help_text="Id of the engine type")  # Id of the engine type
    type_name = models.CharField(max_length=250, unique=True, help_text="Name of the engine type")   # Name of the engine type
    description = models.TextField(null=True, blank=True, help_text="Description of the engine type") # Description of the engine type
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time of creation")       # Date and time of creation
    updated_at = models.DateTimeField(auto_now=True, help_text="Date and time of last update")         # Date and time of last update

    def __str__(self):
        return self.type_name

class AircraftType(models.Model):
    type_id = models.CharField(max_length=20, primary_key=True, help_text="Id of the aircraft type")    # Aircraft type id
    type_name = models.CharField(max_length=50, unique=True, help_text="Name of the aircraft type")   # AirCraft Type Name
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time of creation")       # Date and time of creation
    updated_at = models.DateTimeField(auto_now=True, help_text="Date and time of last update")         # Date and time of last update

    def __str__(self):
        return str(self.type_name)
class AircraftStatusType(models.Model):
    type_id = models.CharField(max_length=20, primary_key=True, help_text="Id of the aircraft type")    # Aircraft type id
    type_name = models.CharField(max_length=50, unique=True, help_text="Name of the aircraft type")   # AirCraft Type Name
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time of creation")       # Date and time of creation
    updated_at = models.DateTimeField(auto_now=True, help_text="Date and time of last update")         # Date and time of last update

    def __str__(self):
        return str(self.type_name)
    
class Aircraft(models.Model):
    """
    Model representing an aircraft.
    """
    aircraft_id = models.CharField(max_length=20, primary_key=True, help_text="Id of the aircraft") # Aircraft Id
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, related_name="airline_aircrafts", help_text="Airline owning the aircraft")  # Airline owning the aircraft
    model_name = models.CharField(max_length=100, help_text="Name of the aircraft model")             # Name of the aircraft model
    aircraft_type_name = models.ForeignKey(AircraftType, on_delete=models.CASCADE, related_name="aircraft_type_name", help_text="Type of the aircraft")  # Type of the aircraft
    manufacturer = models.CharField(max_length=100, help_text="Manufacturer of the aircraft")          # Manufacturer of the aircraft
    registration_number = models.CharField(max_length=20, unique=True, help_text="Registration number of the aircraft")  # Registration number of the aircraft
    seating_capacity = models.PositiveIntegerField(help_text="Seating capacity of the aircraft")      # Seating capacity of the aircraft
    maximum_speed = models.DecimalField(max_digits=6, decimal_places=2, help_text="Maximum speed of the aircraft")        # Maximum speed of the aircraft
    maximum_range = models.DecimalField(max_digits=10, decimal_places=2, help_text="Maximum range of the aircraft")      # Maximum range of the aircraft
    manufacture_date = models.DateField(help_text="date of manufacture of the aircraft")  # date of manufacture of the aircraft
    last_maintenance_date = models.DateField(help_text="last date of maintenance of the aircraft")  # last date of maintenance of the aircraft
    engine_type = models.ForeignKey(EngineType, on_delete=models.CASCADE, related_name='aircrafts', help_text="Type of engine used in the aircraft")  # Type of engine used in the aircraft
    engines_count = models.PositiveIntegerField(help_text="Number of engines in the aircraft")        # Number of engines in the aircraft
    first_class_seats = models.PositiveIntegerField(null=True, blank=True, help_text="Number of first class seats in the aircraft")    # Number of first class seats in the aircraft
    business_class_seats = models.PositiveIntegerField(null=True, blank=True, help_text="Number of business class seats in the aircraft")  # Number of business class seats in the aircraft
    economy_class_seats = models.PositiveIntegerField(null=True, blank=True, help_text="Number of economy class seats in the aircraft")  # Number of economy class seats in the aircraft
    current_status = models.ForeignKey(AircraftStatusType,null=True, on_delete=models.CASCADE, related_name='aircraft_status_type', help_text='Current Status type of aircraft.')
    
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time of creation")      # Date and time of creation
    updated_at = models.DateTimeField(auto_now=True, help_text="Date and time of last update")        # Date and time of last update

    def __str__(self):
        return f"{self.airline.name}"
class StaffPositionType(models.Model):
    """
    Model representing the Staff Position Type
    """
    sp_type_id = models.CharField(max_length=20, primary_key=True, help_text="Staff position type id") # Staff Position Type Id
    position_type = models.CharField(max_length=250,unique=True, help_text="Staff Position Type")   # Staff Potision Type Creation
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time of creation")      # Date and time of creation
    updated_at = models.DateTimeField(auto_now=True, help_text="Date and time of last update")        # Date and time of last update

    def __str__(self):
        return f"{self.position_type}"
    
class Staff(models.Model):
    """
    Model representing staff members.
    """
    staff_id = models.CharField(max_length=20, primary_key=True, help_text="Staff id should be always unique")  # Staff Id 
    user = models.OneToOneField(User, on_delete=models.CASCADE, help_text="User associated with the staff")   # User associated with the staff
    position = models.ForeignKey(StaffPositionType, on_delete=models.CASCADE, help_text="Position of the staff")  # Position of the staff
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, help_text="Airline employing the staff") # Airline employing the staff
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time of creation")    # Date and time of creation
    updated_at = models.DateTimeField(auto_now=True, help_text="Date and time of last update")      # Date and time of last update

    def __str__(self):
        return self.user.email


class Airport(models.Model):
    """
    Model representing an airport.
    """
    airport_id = models.AutoField(primary_key=True, help_text="Id of the airport")               # ID of the airport
    code = models.CharField(max_length=5, unique=True, help_text="Code of the airport IATA cide")               # Code of the airport
    name = models.CharField(max_length=100, unique=True, help_text="Name of the airport")                         # Name of the airport
    country = models.ForeignKey(Country, on_delete=models.CASCADE, help_text="Name of the country")  # Country where the airport is located
    county_or_state = models.ForeignKey(CountyOrState, on_delete=models.CASCADE, help_text="Name of the county or state")  # county or state where the airport is located
    city = models.ForeignKey(City, on_delete=models.CASCADE, help_text="Name of the city")  # city where the airport is located
    latitude = models.DecimalField(max_digits=9, decimal_places=6, help_text="Latitude of the airport")  # Latitude of the airport
    longitude = models.DecimalField(max_digits=9, decimal_places=6, help_text="Longitude of the airport")  # Longitude of the airport
    
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time of creation")      # Date and time of creation
    updated_at = models.DateTimeField(auto_now=True, help_text="Date and time of last update")        # Date and time of last update

    def __str__(self):
        return f"{self.name} ({self.code})"
    
class FlightRegistration(models.Model):
    flight_number = models.CharField(max_length=20,primary_key=True)
    departure_time = models.TimeField(help_text='Flight Departued Time',null=True)
    arrival_time = models.TimeField(help_text='Flight Departued Time',null=True)
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time of creation")      # Date and time of creation
    updated_at = models.DateTimeField(auto_now=True, help_text="Date and time of last update")        # Date and time of last update

class SeatMapping(models.Model):
    flight_number = models.ForeignKey(FlightRegistration, verbose_name=_("Flight Number"), on_delete=models.CASCADE, related_name='flight_number_for_seat') 
    seat_row_id = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time of creation")      # Date and time of creation
    updated_at = models.DateTimeField(auto_now=True, help_text="Date and time of last update")        # Date and time of last update


# Extra models as sir given today 12th apr 2024

class DistanceType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50, unique=True, help_text="enter valid distance type name")

    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time of creation")      # Date and time of creation
    updated_at = models.DateTimeField(auto_now=True, help_text="Date and time of last update")        # Date and time of last update

    def __str__(self):
        return str(self.type_name)
    
class Routes(models.Model):
    route_id = models.CharField(max_length=50,primary_key=True)
    departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departure_airport_for_route')
    arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrival_airport_for_route')
    distance_type = models.ForeignKey(DistanceType, on_delete=models.CASCADE, related_name='distance_type')
    distance_value = models.DecimalField(max_digits=10, decimal_places=5, help_text="distance in miles or kilimeter")
    estimated_flight_time = models.DurationField()
    route_status = models.CharField(max_length=20, choices=(('Active', 'Active'), ('Inactive', 'Inactive')))
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time of creation")      # Date and time of creation
    updated_at = models.DateTimeField(auto_now=True, help_text="Date and time of last update")        # Date and time of last update

    def __str__(self):
        return str(self.route_id)
    
class DayOfOperation(models.Model):
    day_id = models.AutoField(primary_key=True)
    day_name = models.CharField(max_length=15, unique=True, null=False)   

    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time of creation")      # Date and time of creation
    updated_at = models.DateTimeField(auto_now=True, help_text="Date and time of last update")        # Date and time of last update
 
    def __str__(self):
        return str(self.day_name)
        
class FlightFrequencies(models.Model):
    frequency_id = models.AutoField(primary_key=True)
    route = models.ForeignKey(Routes, on_delete=models.CASCADE, related_name='route')
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    days_of_operation = models.ManyToManyField(DayOfOperation, related_name='day_of_operations')
    aircraft_type_id = models.ForeignKey(Aircraft, on_delete=models.CASCADE, related_name="aircraft_type_id")
    flight_status = models.CharField(max_length=20, choices=(('Scheduled', 'Scheduled'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed')))
    
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time of creation")      # Date and time of creation
    updated_at = models.DateTimeField(auto_now=True, help_text="Date and time of last update")        # Date and time of last update

    def __str__(self):
        return str(self.frequency_id)
 
class CrewType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50,unique=True)
    description = models.TextField(null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time of creation")      # Date and time of creation
    updated_at = models.DateTimeField(auto_now=True, help_text="Date and time of last update")        # Date and time of last update
 
    def __str__(self):
        return str(self.type_name)
    
class CrewActiveStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=50, unique=True)


    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time of creation")      # Date and time of creation
    updated_at = models.DateTimeField(auto_now=True, help_text="Date and time of last update")        # Date and time of last update
 
    def __str__(self):
        return str(self.status_name)
    
class Crew(models.Model):
    crew_id = models.AutoField(primary_key=True)
    crew_type = models.ForeignKey(CrewType, on_delete=models.CASCADE, related_name='crew_type')
    crew_name = models.CharField(max_length=255, unique=True)
    license_certification_info = models.CharField(max_length=255)
    # license certification info 
    license_certification_id = models.CharField(max_length=30, unique=True)
    license_certification_name = models.CharField(max_length=50)
    license_certification_valid_upto = models.DateField()
    
    base_location = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='airport_as_base_location')
    # contact information
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    
    active_status = models.ForeignKey(CrewActiveStatus, on_delete=models.CASCADE, related_name='crew_active_status')

    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time of creation")      # Date and time of creation
    updated_at = models.DateTimeField(auto_now=True, help_text="Date and time of last update")        # Date and time of last update

    def __str__(self):
        return self.crew_name
    
class FlightRequirements(models.Model):
    requirement_id = models.AutoField(primary_key=True)
    route_id = models.ForeignKey(Routes, on_delete=models.CASCADE, related_name='flight_req_routes')
    aircraft_type_id = models.ForeignKey(AircraftType, on_delete=models.CASCADE, related_name='aircraft_type_id_flight_req')
    minimum_crew_members = models.PositiveIntegerField()
    maximum_cargo_weight = models.DecimalField(max_digits=10, decimal_places=2)
    special_equipment_needed = models.CharField(max_length=255)
    additional_considerations = models.TextField()

    def __str__(self):
        return f"Flight Requirement {self.requirement_id} for {self.route_id}"
    

class FlightSchedule(models.Model):
    """
    Model representing a flight.    
    """
    schedule_id = models.CharField(max_length=20, primary_key=True, help_text="Unique identifier for the flight scheduled id")  # Unique identifier for the flight schedule id
    flight_number = models.CharField(max_length=20, unique=True, help_text="Unique identifier for the flight id")  # Unique identifier for the flight id
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE, help_text="Aircraft assigned to the flight")  # Aircraft assigned to the flight
    route = models.ForeignKey(Routes, null=True, on_delete=models.CASCADE, related_name='routes_for_flight_schedule') # Route Of Flight
    frequency = models.ForeignKey(FlightFrequencies, null=True, on_delete=models.CASCADE, related_name='frequency_of_routes_for_flight_schedule') # Frequency Of the Route Of for Flight Scheduling
    staff = models.ManyToManyField(Staff, help_text="Staff assigned to the flight")               # Staff assigned to the flight
    SCHEDULE_TYPE = (
        ('specific_date','specific_date'),
        ('date_range','date_range'),
    )
    schedule_type = models.CharField(max_length=20, choices=SCHEDULE_TYPE, null=True, help_text='Select the Schedule type for scheduling the flight')
    specific_date = models.DateField(help_text='Select Specific Date', null=True, blank=True)
    from_date = models.DateField(help_text='Select From Date', null=True, blank=True)
    end_date = models.DateField(help_text='Select End Date', null=True, blank=True)
    status = models.CharField(max_length=20, choices=(
        ('Scheduled', 'Scheduled'),
        ('Departed', 'Departed'),
        ('In Air', 'In Air'),
        ('Arrived', 'Arrived'),
        ('Cancelled', 'Cancelled'),
    ), help_text="Status of the flight")  # Status of the flight
    notes = models.TextField(null=True, blank=True, help_text="Additional notes about the flight")  # Additional notes about the flight
    ticket_price = models.DecimalField(max_digits=10,decimal_places=2, help_text="ticket price for the flight")
    
    created_at = models.DateTimeField(auto_now_add=True, help_text="Date and time of creation")      # Date and time of creation
    updated_at = models.DateTimeField(auto_now=True, help_text="Date and time of last update")        # Date and time of last update

    def __str__(self):
        return self.flight_number
class FlightScheduleDetails(models.Model):
    flight_scheduled_id = models.CharField(max_length=50, primary_key=True,)
    schedule_ref_id = models.ForeignKey(FlightSchedule, on_delete=models.CASCADE, related_name='flight_schedule_ref_id')
    scheduled_date = models.DateField()
    scheduled_day = models.DateField()
    # will add more column here as per requirementd



