# Generated by Django 4.2.11 on 2024-04-13 05:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('phone_no', models.CharField(max_length=15)),
                ('nationality', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('aircraft_id', models.CharField(help_text='Id of the aircraft', max_length=20, primary_key=True, serialize=False)),
                ('model_name', models.CharField(help_text='Name of the aircraft model', max_length=100)),
                ('manufacturer', models.CharField(help_text='Manufacturer of the aircraft', max_length=100)),
                ('registration_number', models.CharField(help_text='Registration number of the aircraft', max_length=20, unique=True)),
                ('seating_capacity', models.PositiveIntegerField(help_text='Seating capacity of the aircraft')),
                ('maximum_speed', models.DecimalField(decimal_places=2, help_text='Maximum speed of the aircraft', max_digits=6)),
                ('maximum_range', models.DecimalField(decimal_places=2, help_text='Maximum range of the aircraft', max_digits=10)),
                ('manufacture_date', models.DateField(help_text='date of manufacture of the aircraft')),
                ('last_maintenance_date', models.DateField(help_text='last date of maintenance of the aircraft')),
                ('engines_count', models.PositiveIntegerField(help_text='Number of engines in the aircraft')),
                ('first_class_seats', models.PositiveIntegerField(blank=True, help_text='Number of first class seats in the aircraft', null=True)),
                ('business_class_seats', models.PositiveIntegerField(blank=True, help_text='Number of business class seats in the aircraft', null=True)),
                ('economy_class_seats', models.PositiveIntegerField(blank=True, help_text='Number of economy class seats in the aircraft', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date and time of creation')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date and time of last update')),
            ],
        ),
        migrations.CreateModel(
            name='AircraftStatusType',
            fields=[
                ('type_id', models.CharField(help_text='Id of the aircraft type', max_length=20, primary_key=True, serialize=False)),
                ('type_name', models.CharField(help_text='Name of the aircraft type', max_length=50, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date and time of creation')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date and time of last update')),
            ],
        ),
        migrations.CreateModel(
            name='AircraftType',
            fields=[
                ('type_id', models.CharField(help_text='Id of the aircraft type', max_length=20, primary_key=True, serialize=False)),
                ('type_name', models.CharField(help_text='Name of the aircraft type', max_length=50, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date and time of creation')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date and time of last update')),
            ],
        ),
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('airline_id', models.CharField(help_text='Id of the airline', max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Name of the airline', max_length=100, unique=True)),
                ('code', models.CharField(help_text='Code of the airline', max_length=3, unique=True)),
                ('logo', models.ImageField(blank=True, help_text='Logo of the airline', null=True, upload_to='airline_logos/')),
                ('contact_person', models.CharField(help_text='Contact person of the airline', max_length=100)),
                ('email', models.EmailField(help_text='Email of the airline', max_length=254)),
                ('phone_number', models.CharField(help_text='Phone number of the airline', max_length=20)),
                ('address', models.TextField(help_text='Address of the airline')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date and time of creation')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date and time of last update')),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('airport_id', models.AutoField(help_text='Id of the airport', primary_key=True, serialize=False)),
                ('code', models.CharField(help_text='Code of the airport IATA cide', max_length=5, unique=True)),
                ('name', models.CharField(help_text='Name of the airport', max_length=100, unique=True)),
                ('latitude', models.DecimalField(decimal_places=6, help_text='Latitude of the airport', max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, help_text='Longitude of the airport', max_digits=9)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date and time of creation')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date and time of last update')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('code', models.CharField(help_text='Code of the country', max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Name of the country', max_length=50, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date and time of creation')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date and time of last update')),
            ],
        ),
        migrations.CreateModel(
            name='CrewActiveStatus',
            fields=[
                ('status_id', models.AutoField(primary_key=True, serialize=False)),
                ('status_name', models.CharField(max_length=50, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date and time of creation')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date and time of last update')),
            ],
        ),
        migrations.CreateModel(
            name='CrewType',
            fields=[
                ('type_id', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date and time of creation')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date and time of last update')),
            ],
        ),
        migrations.CreateModel(
            name='DayOfOperation',
            fields=[
                ('day_id', models.AutoField(primary_key=True, serialize=False)),
                ('day_name', models.CharField(max_length=15, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date and time of creation')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date and time of last update')),
            ],
        ),
        migrations.CreateModel(
            name='DistanceType',
            fields=[
                ('type_id', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(help_text='enter valid distance type name', max_length=50, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date and time of creation')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date and time of last update')),
            ],
        ),
        migrations.CreateModel(
            name='EngineType',
            fields=[
                ('type_id', models.CharField(help_text='Id of the engine type', max_length=20, primary_key=True, serialize=False)),
                ('type_name', models.CharField(help_text='Name of the engine type', max_length=250, unique=True)),
                ('description', models.TextField(blank=True, help_text='Description of the engine type', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date and time of creation')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date and time of last update')),
            ],
        ),
        migrations.CreateModel(
            name='FlightRegistration',
            fields=[
                ('flight_number', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date and time of creation')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date and time of last update')),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name_of_the_airline', to='bookingapp.airline', verbose_name='Airline')),
            ],
        ),
        migrations.CreateModel(
            name='ModuleRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_name', models.CharField(max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MSRegistration',
            fields=[
                ('mservice_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('mservice_name', models.CharField(max_length=100)),
                ('arguments', models.JSONField(blank=True, null=True)),
                ('arguments_list', models.TextField(blank=True, null=True)),
                ('required_parameter', models.TextField(blank=True, null=True)),
                ('optional_parameter', models.TextField(blank=True, null=True)),
                ('is_authenticate', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('region_id', models.CharField(help_text='Id of the region', max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Name of the region', max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date and time of creation')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date and time of last update')),
            ],
        ),
        migrations.CreateModel(
            name='StaffPositionType',
            fields=[
                ('sp_type_id', models.CharField(help_text='Staff position type id', max_length=20, primary_key=True, serialize=False)),
                ('position_type', models.CharField(help_text='Staff Position Type', max_length=250, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date and time of creation')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date and time of last update')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.CharField(help_text='Staff id should be always unique', max_length=20, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date and time of creation')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date and time of last update')),
                ('airline', models.ForeignKey(help_text='Airline employing the staff', on_delete=django.db.models.deletion.CASCADE, to='bookingapp.airline')),
                ('position', models.ForeignKey(help_text='Position of the staff', on_delete=django.db.models.deletion.CASCADE, to='bookingapp.staffpositiontype')),
                ('user', models.OneToOneField(help_text='User associated with the staff', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SeatMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_row_id', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date and time of creation')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date and time of last update')),
                ('flight_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flight_number_for_seat', to='bookingapp.flightregistration', verbose_name='Flight Number')),
            ],
        ),
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('route_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('distance_value', models.DecimalField(decimal_places=5, help_text='distance in miles or kilimeter', max_digits=10)),
                ('estimated_flight_time', models.DurationField()),
                ('route_status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date and time of creation')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date and time of last update')),
                ('arrival_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival_airport_for_route', to='bookingapp.airport')),
                ('departure_airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure_airport_for_route', to='bookingapp.airport')),
                ('distance_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='distance_type', to='bookingapp.distancetype')),
            ],
        ),
        migrations.CreateModel(
            name='MsToModuleMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('module_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='module_id', to='bookingapp.moduleregistration')),
                ('mservice_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ms_id', to='bookingapp.msregistration')),
            ],
        ),
        migrations.CreateModel(
            name='FlightSchedule',
            fields=[
                ('schedule_id', models.CharField(help_text='Unique identifier for the flight scheduled id', max_length=20, primary_key=True, serialize=False)),
                ('flight_number', models.CharField(help_text='Unique identifier for the flight id', max_length=20, unique=True)),
                ('departure_time', models.DateTimeField(help_text='Scheduled departure time')),
                ('arrival_time', models.DateTimeField(help_text='Scheduled arrival time')),
                ('status', models.CharField(choices=[('Scheduled', 'Scheduled'), ('Departed', 'Departed'), ('In Air', 'In Air'), ('Arrived', 'Arrived'), ('Cancelled', 'Cancelled')], help_text='Status of the flight', max_length=20)),
                ('duration', models.DurationField(blank=True, help_text='Duration of the flight', null=True)),
                ('distance', models.DecimalField(blank=True, decimal_places=2, help_text='Distance of the flight', max_digits=10, null=True)),
                ('delay_reason', models.TextField(blank=True, help_text='Reason for flight delay', null=True)),
                ('gate', models.PositiveBigIntegerField(blank=True, help_text='Enter the gate number', null=True)),
                ('notes', models.TextField(blank=True, help_text='Additional notes about the flight', null=True)),
                ('total_seat', models.PositiveIntegerField(default=30, help_text='total seat of the flight')),
                ('ticket_price', models.DecimalField(decimal_places=2, help_text='ticket price for the flight', max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date and time of creation')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date and time of last update')),
                ('aircraft', models.ForeignKey(help_text='Aircraft assigned to the flight', on_delete=django.db.models.deletion.CASCADE, to='bookingapp.aircraft')),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airline_name', to='bookingapp.airline')),
                ('arrival_airport', models.ForeignKey(help_text='Airport of arrival', on_delete=django.db.models.deletion.CASCADE, related_name='arrivals', to='bookingapp.airport')),
                ('departure_airport', models.ForeignKey(help_text='Airport of departure', on_delete=django.db.models.deletion.CASCADE, related_name='departures', to='bookingapp.airport')),
                ('staff', models.ManyToManyField(help_text='Staff assigned to the flight', to='bookingapp.staff')),
            ],
        ),
        migrations.CreateModel(
            name='FlightRequirements',
            fields=[
                ('requirement_id', models.AutoField(primary_key=True, serialize=False)),
                ('minimum_crew_members', models.PositiveIntegerField()),
                ('maximum_cargo_weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('special_equipment_needed', models.CharField(max_length=255)),
                ('additional_considerations', models.TextField()),
                ('aircraft_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aircraft_type_id_flight_req', to='bookingapp.aircrafttype')),
                ('route_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flight_req_routes', to='bookingapp.routes')),
            ],
        ),
        migrations.CreateModel(
            name='FlightFrequencies',
            fields=[
                ('frequency_id', models.AutoField(primary_key=True, serialize=False)),
                ('departure_time', models.TimeField()),
                ('arrival_time', models.TimeField()),
                ('flight_status', models.CharField(choices=[('Scheduled', 'Scheduled'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date and time of creation')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date and time of last update')),
                ('aircraft_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aircraft_type_id', to='bookingapp.aircraft')),
                ('days_of_operation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='day_of_operations', to='bookingapp.dayofoperation')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route', to='bookingapp.routes')),
            ],
        ),
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('crew_id', models.AutoField(primary_key=True, serialize=False)),
                ('crew_name', models.CharField(max_length=255, unique=True)),
                ('license_certification_info', models.CharField(max_length=255)),
                ('license_certification_id', models.CharField(max_length=30, unique=True)),
                ('license_certification_name', models.CharField(max_length=50)),
                ('license_certification_valid_upto', models.DateField()),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date and time of creation')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date and time of last update')),
                ('active_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crew_active_status', to='bookingapp.crewactivestatus')),
                ('base_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airport_as_base_location', to='bookingapp.airport')),
                ('crew_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crew_type', to='bookingapp.crewtype')),
            ],
        ),
        migrations.CreateModel(
            name='CountyOrState',
            fields=[
                ('code', models.CharField(help_text='Code of the country', max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Name of the county/state', max_length=50, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date and time of creation')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date and time of last update')),
                ('county', models.ForeignKey(help_text='Name of the country', on_delete=django.db.models.deletion.CASCADE, to='bookingapp.country')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('code', models.CharField(help_text='Code of the city', max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Name of the city', max_length=50, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date and time of creation')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date and time of last update')),
                ('country', models.ForeignKey(help_text='Name of the country', on_delete=django.db.models.deletion.CASCADE, to='bookingapp.country')),
                ('county_or_state', models.ForeignKey(help_text='Name of the county or state', on_delete=django.db.models.deletion.CASCADE, to='bookingapp.countyorstate')),
            ],
        ),
        migrations.AddField(
            model_name='airport',
            name='city',
            field=models.ForeignKey(help_text='Name of the city', on_delete=django.db.models.deletion.CASCADE, to='bookingapp.city'),
        ),
        migrations.AddField(
            model_name='airport',
            name='country',
            field=models.ForeignKey(help_text='Name of the country', on_delete=django.db.models.deletion.CASCADE, to='bookingapp.country'),
        ),
        migrations.AddField(
            model_name='airport',
            name='county_or_state',
            field=models.ForeignKey(help_text='Name of the county or state', on_delete=django.db.models.deletion.CASCADE, to='bookingapp.countyorstate'),
        ),
        migrations.AddField(
            model_name='airline',
            name='operating_regions',
            field=models.ManyToManyField(help_text='Regions where the airline operates', to='bookingapp.region'),
        ),
        migrations.AddField(
            model_name='aircraft',
            name='aircraft_type',
            field=models.ForeignKey(help_text='Type of the aircraft', on_delete=django.db.models.deletion.CASCADE, related_name='aircraft_type_name', to='bookingapp.aircrafttype'),
        ),
        migrations.AddField(
            model_name='aircraft',
            name='airline',
            field=models.ForeignKey(help_text='Airline owning the aircraft', on_delete=django.db.models.deletion.CASCADE, related_name='airline_aircrafts', to='bookingapp.airline'),
        ),
        migrations.AddField(
            model_name='aircraft',
            name='current_status',
            field=models.ForeignKey(help_text='Current Status type of aircraft.', on_delete=django.db.models.deletion.CASCADE, related_name='aircraft_status_type', to='bookingapp.aircraftstatustype'),
        ),
        migrations.AddField(
            model_name='aircraft',
            name='engine_type',
            field=models.ForeignKey(help_text='Type of engine used in the aircraft', on_delete=django.db.models.deletion.CASCADE, related_name='aircrafts', to='bookingapp.enginetype'),
        ),
    ]
