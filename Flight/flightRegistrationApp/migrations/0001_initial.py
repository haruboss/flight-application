# Generated by Django 3.2.6 on 2021-08-31 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('source_city', models.CharField(max_length=50)),
                ('destination_city', models.CharField(max_length=50)),
                ('departure_date', models.DateField()),
                ('departure_time', models.TimeField()),
                ('flight_charges', models.PositiveIntegerField()),
            ],
        ),
    ]
