from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Flight
from django.views.generic import CreateView
from .forms import *
    
def Home(request):
    return render(request, 'flightRegistrationApp/home.html')

class flightCreateView(CreateView):
    template_name = 'index.html'
    form_class = FlightCreateForm
    success_url = reverse_lazy('flightRegistrationApp:home')

   