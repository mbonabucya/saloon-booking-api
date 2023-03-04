from django.urls import path
from .views import SalonList, SalonDetail, StylistList, StylistDetail, BookingList, BookingDetail

urlpatterns = [
    path('salons/', SalonList.as_view()),
    path('salons/<int:pk>/', SalonDetail.as_view()),
    path('stylists/', StylistList.as_view()),
    path('stylists/<int:pk>/', StylistDetail.as_view()),
    path('bookings/', BookingList.as_view()),
    path('bookings/<int:pk>/', BookingDetail.as_view()),
]
