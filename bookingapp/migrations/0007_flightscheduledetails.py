# Generated by Django 4.2.11 on 2024-04-16 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0006_remove_flightfrequencies_days_of_operation_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlightScheduleDetails',
            fields=[
                ('flight_scheduled_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('scheduled_date', models.DateField()),
                ('scheduled_day', models.DateField()),
                ('schedule_ref_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flight_schedule_ref_id', to='bookingapp.flightschedule')),
            ],
        ),
    ]