from django.contrib import admin
from bookingapp import admin_master_general

# Inside admin.py

from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import *

# Define ModelResource classes for each model
class RegionResource(resources.ModelResource):
    class Meta:
        model = Region
        import_id_fields = ['region_id']
        fields = ('region_id', 'name', 'created_at', 'updated_at')

class AirlineResource(resources.ModelResource):
    class Meta:
        model = Airline
        import_id_fields = ['airline_id']
        fields = ('airline_id', 'name', 'code', 'contact_person', 'email', 'phone_number', 'address', 'created_at', 'updated_at')

class EngineTypeResource(resources.ModelResource):
    class Meta:
        model = EngineType
        import_id_fields = ['type_id']
        fields = ('type_id', 'type_name', 'description', 'created_at', 'updated_at')

class AircraftTypeResource(resources.ModelResource):
    class Meta:
        model = AircraftType
        import_id_fields = ['type_id']
        fields = ('type_id', 'type_name', 'created_at', 'updated_at')

class AircraftResource(resources.ModelResource):
    class Meta:
        model = Aircraft
        import_id_fields = ['aircraft_id']
        fields = ('aircraft_id', 'airline', 'model_name', 'aircraft_type_name', 'manufacturer', 'registration_number', 'seating_capacity', 'maximum_speed', 'maximum_range', 'manufacture_date', 'last_maintenance_date', 'engine_type', 'engines_count', 'first_class_seats', 'business_class_seats', 'economy_class_seats', 'created_at', 'updated_at')

class StaffPositionTypeResource(resources.ModelResource):
    class Meta:
        model = StaffPositionType
        import_id_fields = ['sp_type_id']
        fields = ('sp_type_id', 'position_type', 'created_at', 'updated_at')

class StaffResource(resources.ModelResource):
    class Meta:
        model = Staff
        import_id_fields = ['staff_id']
        fields = ('staff_id', 'user', 'position', 'airline', 'created_at', 'updated_at')

class AirportResource(resources.ModelResource):
    class Meta:
        model = Airport
        import_id_fields = ['code']
        fields = ('code', 'name', 'country', 'county_or_state', 'city', 'latitude', 'longitude', 'created_at', 'updated_at')

class FlightScheduleResource(resources.ModelResource):
    class Meta:
        model = FlightSchedule
        import_id_fields = ['schedule_id']
        fields = ('schedule_id','flight_number', 'aircraft', 'route', 'frequency', 'status', 'notes', 'ticket_price', 'created_at', 'updated_at')

# Register your models with their respective custom admin classes
@admin.register(Region)
class RegionAdmin(ImportExportModelAdmin):
    list_display = ('region_id', 'name', 'created_at', 'updated_at')
    resource_class = RegionResource

@admin.register(Airline)
class AirlineAdmin(ImportExportModelAdmin):
    list_display = ('airline_id', 'name', 'code', 'contact_person', 'email', 'phone_number', 'address', 'created_at', 'updated_at')
    resource_class = AirlineResource

@admin.register(EngineType)
class EngineTypeAdmin(ImportExportModelAdmin):
    list_display = ('type_id', 'type_name', 'description', 'created_at', 'updated_at')
    resource_class = EngineTypeResource

@admin.register(AircraftType)
class AircraftTypeAdmin(ImportExportModelAdmin):
    list_display = ('type_id', 'type_name', 'created_at', 'updated_at')
    resource_class = AircraftTypeResource

@admin.register(Aircraft)
class AircraftAdmin(ImportExportModelAdmin):
    list_display = ('aircraft_id', 'airline', 'model_name', 'aircraft_type_name', 'manufacturer', 'registration_number', 'seating_capacity', 'maximum_speed', 'maximum_range', 'manufacture_date', 'last_maintenance_date', 'engine_type', 'engines_count', 'first_class_seats', 'business_class_seats', 'economy_class_seats', 'created_at', 'updated_at')
    resource_class = AircraftResource

@admin.register(StaffPositionType)
class StaffPositionTypeAdmin(ImportExportModelAdmin):
    list_display = ('sp_type_id', 'position_type', 'created_at', 'updated_at')
    resource_class = StaffPositionTypeResource

@admin.register(Staff)
class StaffAdmin(ImportExportModelAdmin):
    list_display = ('staff_id', 'user', 'position', 'airline', 'created_at', 'updated_at')
    resource_class = StaffResource

@admin.register(Airport)
class AirportAdmin(ImportExportModelAdmin):
    list_display = ('code', 'name', 'country', 'county_or_state', 'city', 'latitude', 'longitude', 'created_at', 'updated_at')
    resource_class = AirportResource
    list_filter = ["code","name"]


@admin.register(FlightSchedule)
class FlightScheduleAdmin(ImportExportModelAdmin):
    list_display = ('schedule_id','flight_number', 'aircraft', 'route', 'frequency', 'status', 'notes', 'ticket_price', 'created_at', 'updated_at')
    resource_class = FlightScheduleResource

class MSRegistrationResource(resources.ModelResource):
    class Meta:
        model = MSRegistration
        import_id_fields = ['mservice_id']
        fields = ('mservice_id', 'mservice_name', 'arguments', 'arguments_list', 'required_parameter', 'optional_parameter', 'is_authenticate', 'created_at', 'updated_at')

class ModuleRegistrationResource(resources.ModelResource):
    class Meta:
        model = ModuleRegistration
        import_id_fields = ['id']
        fields = ('id', 'module_name', 'created_at', 'updated_at')

class MsToModuleMappingResource(resources.ModelResource):
    class Meta:
        model = MsToModuleMapping
        fields = ('mservice_id', 'module_id', 'created_at', 'updated_at')

# Register your models with their respective custom admin classes
@admin.register(MSRegistration)
class MSRegistrationAdmin(ImportExportModelAdmin):
    list_display = ('mservice_id', 'mservice_name', 'arguments', 'arguments_list', 'required_parameter', 'optional_parameter', 'is_authenticate', 'created_at', 'updated_at')
    resource_class = MSRegistrationResource

@admin.register(ModuleRegistration)
class ModuleRegistrationAdmin(ImportExportModelAdmin):
    list_display = ('id', 'module_name', 'created_at', 'updated_at')
    resource_class = ModuleRegistrationResource

@admin.register(MsToModuleMapping)
class MsToModuleMappingAdmin(ImportExportModelAdmin):
    list_display = ('mservice_id', 'module_id', 'created_at', 'updated_at')
    resource_class = MsToModuleMappingResource

class DistanceTypeResource(resources.ModelResource):
    class Meta:
        model = DistanceType
        fields = ('type_id', 'type_name', 'created_at', 'updated_at')
        import_id_fields = ('type_id',)

class RoutesResource(resources.ModelResource):
    class Meta:
        model = Routes
        fields = ('route_id', 'departure_airport', 'arrival_airport', 'distance_type', 'distance_value', 'estimated_flight_time', 'route_status', 'created_at', 'updated_at')
        import_id_fields = ('route_id',)

class DayOfOperationResource(resources.ModelResource):
    class Meta:
        model = DayOfOperation
        fields = ('day_id', 'day_name', 'created_at', 'updated_at')
        import_id_fields = ('day_id',)

class FlightFrequenciesResource(resources.ModelResource):
    class Meta:
        model = FlightFrequencies
        fields = ('frequency_id', 'route', 'departure_time', 'arrival_time', 'aircraft_type_id', 'flight_status', 'created_at', 'updated_at')
        import_id_fields = ('frequency_id',)

class CrewTypeResource(resources.ModelResource):
    class Meta:
        model = CrewType
        fields = ('type_id', 'type_name', 'description', 'created_at', 'updated_at')
        import_id_fields = ('type_id',)

class CrewActiveStatusResource(resources.ModelResource):
    class Meta:
        model = CrewActiveStatus
        fields = ('status_id', 'status_name', 'created_at', 'updated_at')
        import_id_fields = ('status_id',)

class CrewResource(resources.ModelResource):
    class Meta:
        model = Crew
        fields = ('crew_id', 'crew_type', 'crew_name', 'license_certification_info', 'license_certification_id', 'license_certification_name', 'license_certification_valid_upto', 'base_location', 'phone_number', 'email', 'active_status', 'created_at', 'updated_at')
        import_id_fields = ('crew_id',)

class FlightRequirementsResource(resources.ModelResource):
    class Meta:
        model = FlightRequirements
        fields = ('requirement_id', 'route_id', 'aircraft_type_id', 'minimum_crew_members', 'maximum_cargo_weight', 'special_equipment_needed', 'additional_considerations')
        import_id_fields = ('requirement_id',)

class AircraftStatusTypeResource(resources.ModelResource):
    class Meta:
        model = AircraftStatusType
        fields = ('type_id', 'type_name', 'created_at', 'updated_at')

        import_id_fields = ('type_id',)

@admin.register(DistanceType)
class DistanceTypeAdmin(ImportExportModelAdmin):
    resource_class = DistanceTypeResource
    list_display = ('type_id', 'type_name', 'created_at', 'updated_at')

@admin.register(Routes)
class RoutesAdmin(ImportExportModelAdmin):
    resource_class = RoutesResource
    list_display = ('route_id', 'departure_airport', 'arrival_airport', 'distance_type', 'distance_value', 'estimated_flight_time', 'route_status', 'created_at', 'updated_at')

@admin.register(DayOfOperation)
class DayOfOperationAdmin(ImportExportModelAdmin):
    resource_class = DayOfOperationResource
    list_display = ('day_id', 'day_name', 'created_at', 'updated_at')

@admin.register(FlightFrequencies)
class FlightFrequenciesAdmin(ImportExportModelAdmin):
    resource_class = FlightFrequenciesResource
    list_display = ('frequency_id', 'route', 'departure_time', 'arrival_time', 'aircraft_type_id', 'flight_status', 'created_at', 'updated_at')

@admin.register(CrewType)
class CrewTypeAdmin(ImportExportModelAdmin):
    resource_class = CrewTypeResource
    list_display = ('type_id', 'type_name', 'description', 'created_at', 'updated_at')

@admin.register(CrewActiveStatus)
class CrewActiveStatusAdmin(ImportExportModelAdmin):
    resource_class = CrewActiveStatusResource
    list_display = ('status_id', 'status_name', 'created_at', 'updated_at')

@admin.register(Crew)
class CrewAdmin(ImportExportModelAdmin):
    resource_class = CrewResource
    list_display = ('crew_id', 'crew_type', 'crew_name', 'license_certification_info', 'license_certification_id', 'license_certification_name', 'license_certification_valid_upto', 'base_location', 'phone_number', 'email', 'active_status', 'created_at', 'updated_at')

@admin.register(FlightRequirements)
class FlightRequirementsAdmin(ImportExportModelAdmin):
    resource_class = FlightRequirementsResource
    list_display = ('requirement_id', 'route_id', 'aircraft_type_id', 'minimum_crew_members', 'maximum_cargo_weight', 'special_equipment_needed', 'additional_considerations')
@admin.register(AircraftStatusType)
class AircraftStatusTypeAdmin(ImportExportModelAdmin):
    resource_class = AircraftStatusTypeResource
    list_display = ('type_id', 'type_name', 'created_at', 'updated_at')
