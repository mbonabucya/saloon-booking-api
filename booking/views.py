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
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Salon, Stylist, Booking
from .serializers import SalonSerializer, StylistSerializer, BookingSerializer


@api_view(['GET', 'POST'])
def booking_list(request):
    """
    List all bookings, or create a new booking.
    """
    if request.method == 'GET':
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # check if the salon is available at the requested time
        salon = Salon.objects.get(pk=request.data['salon'])
        existing_bookings = Booking.objects.filter(
            salon=salon, start_time=request.data['start_time'], end_time=request.data['end_time'])
        if existing_bookings:
            return Response({'message': 'This salon is already booked at this time'}, status=status.HTTP_400_BAD_REQUEST)
        
        # check if the stylist is available at the requested time
        stylist = Stylist.objects.get(pk=request.data['stylist'])
        existing_bookings = Booking.objects.filter(
            stylist=stylist, start_time=request.data['start_time'], end_time=request.data['end_time'])
        if existing_bookings:
            return Response({'message': 'This stylist is already booked at this time'}, status=status.HTTP_400_BAD_REQUEST)

        # create the new booking
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def booking_detail(request, pk):
    """
    Retrieve, update or delete a booking.
    """
    try:
        booking = Booking.objects.get(pk=pk)
    except Booking.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookingSerializer(booking)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # check if the salon is available at the requested time
        salon = Salon.objects.get(pk=request.data['salon'])
        existing_bookings = Booking.objects.filter(
            salon=salon, start_time=request.data['start_time'], end_time=request.data['end_time']).exclude(pk=pk)
        if existing_bookings:
            return Response({'message': 'This salon is already booked at this time'}, status=status.HTTP_400_BAD_REQUEST)
        
        # check if the stylist is available at the requested time
        stylist = Stylist.objects.get(pk=request.data['stylist'])
        existing_bookings = Booking.objects.filter(
            stylist=stylist, start_time=request.data['start_time'], end_time=request.data['end_time']).exclude(pk=pk)
        if existing_bookings:
            return Response({'message': 'This stylist is already booked at this time'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = BookingSerializer(booking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





