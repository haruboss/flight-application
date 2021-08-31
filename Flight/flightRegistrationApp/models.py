from django.db import models

TRIP_CHOICE =(
    ("One Way", "One Way"),
    ("Round Way", "Round Way"),
)
  

class Flight(models.Model):
    name = models.CharField(max_length=50)
    source_city = models.CharField(max_length=50)
    destination_city = models.CharField(max_length=50)
    trip_category = models.CharField(max_length=50, choices=TRIP_CHOICE, default=None)
    departure_date = models.DateField(auto_now=False)
    departure_time =  models.TimeField(auto_now=False)
    flight_charges = models.PositiveIntegerField()

    def __str__ (self):
        return self.name
