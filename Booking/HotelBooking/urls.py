from django.urls import path
from .views import ReservationView, AllReservationView, ReservationbyUserIdView, ReservationbyUserIdAndBookingIdView


urlpatterns = [
    path('reserve/', ReservationView.as_view(), name = 'reservation'),
    path('allreservation/', AllReservationView.as_view(),name='fetchall'),
    path('allreservation/<int:user>/', ReservationbyUserIdView.as_view(),name='fetchbyid'),
    path('allreservation/<int:user>/<int:id>/', ReservationbyUserIdAndBookingIdView.as_view(),name='fetchbybookingid'),
]
