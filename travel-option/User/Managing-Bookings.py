@login_required
def view_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/view_bookings.html', {'bookings': bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = Booking.objects.get(pk=booking_id, user=request.user)
    booking.status = 'Cancelled'
    booking.travel_option.available_seats += booking.number_of_seats
    booking.travel_option.save()
    booking.save()
    return redirect('view_bookings')
