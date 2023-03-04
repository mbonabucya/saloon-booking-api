from django.shortcuts import render

from rest_framework import generics
from .models import Salon, Stylist, Booking
from .serializers import SalonSerializer, StylistSerializer, BookingSerializer

class SalonList(generics.ListCreateAPIView):
    queryset = Salon.objects.all()
    serializer_class = SalonSerializer

class SalonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Salon.objects.all()
    serializer_class = SalonSerializer

class StylistList(generics.ListCreateAPIView):
    queryset = Stylist.objects.all()
    serializer_class = StylistSerializer

class StylistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stylist.objects.all()
    serializer_class = StylistSerializer

class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer



"""
    Function based views
"""





