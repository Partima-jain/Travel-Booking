from django.shortcuts import render, redirect
from .models import Booking, TravelOption
from django.contrib.auth.decorators import login_required

@login_required
def book_travel(request, travel_id):
    travel_option = TravelOption.objects.get(pk=travel_id)
    if request.method == 'POST':
        seats = int(request.POST['seats'])
        total_price = seats * travel_option.price
        booking = Booking.objects.create(
            user=request.user,
            travel_option=travel_option,
            number_of_seats=seats,
            total_price=total_price,
            status='Confirmed'
        )
        travel_option.available_seats -= seats
        travel_option.save()
        return redirect('view_bookings')
    return render(request, 'bookings/book_travel.html', {'travel_option': travel_option})
