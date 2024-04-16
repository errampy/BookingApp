# Generated by Django 4.2.11 on 2024-04-16 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0003_alter_aircraft_current_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flightregistration',
            name='airline',
        ),
        migrations.RemoveField(
            model_name='flightschedule',
            name='airline',
        ),
        migrations.RemoveField(
            model_name='flightschedule',
            name='arrival_airport',
        ),
        migrations.RemoveField(
            model_name='flightschedule',
            name='arrival_time',
        ),
        migrations.RemoveField(
            model_name='flightschedule',
            name='delay_reason',
        ),
        migrations.RemoveField(
            model_name='flightschedule',
            name='departure_airport',
        ),
        migrations.RemoveField(
            model_name='flightschedule',
            name='departure_time',
        ),
        migrations.RemoveField(
            model_name='flightschedule',
            name='distance',
        ),
        migrations.RemoveField(
            model_name='flightschedule',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='flightschedule',
            name='gate',
        ),
        migrations.RemoveField(
            model_name='flightschedule',
            name='total_seat',
        ),
        migrations.AddField(
            model_name='flightregistration',
            name='arrival_time',
            field=models.TimeField(help_text='Flight Departued Time', null=True),
        ),
        migrations.AddField(
            model_name='flightregistration',
            name='departure_time',
            field=models.TimeField(help_text='Flight Departued Time', null=True),
        ),
        migrations.AddField(
            model_name='flightschedule',
            name='frequency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='frequency_of_routes_for_flight_schedule', to='bookingapp.flightfrequencies'),
        ),
        migrations.AddField(
            model_name='flightschedule',
            name='route',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='routes_for_flight_schedule', to='bookingapp.routes'),
        ),
    ]
