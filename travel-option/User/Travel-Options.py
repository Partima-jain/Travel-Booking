from django.shortcuts import render
from .models import TravelOption

def list_travel_options(request):
    travel_options = TravelOption.objects.all()
    return render(request, 'bookings/travel_options.html', {'travel_options': travel_options})
