from rest_framework import serializers
from .models import Salon, Stylist, Booking

class SalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salon
        fields = '__all__'

class StylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stylist
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
