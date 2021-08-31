
from django.urls import path, include
from .views import *

app_name="flightRegistrationApp"
urlpatterns = [
    path('', Home, name="home"),
    path('flight/add/', flightCreateView.as_view(), name='flight-add'),
]