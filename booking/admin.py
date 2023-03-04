from django.contrib import admin
from .models import *



class SalonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')
    search_fields = ('name',)
admin.site.register(Salon, SalonAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display =('id','stylist','customer_name','appointment_time')
    search_fields = ('stylist',)
admin.site.register(Booking, BookingAdmin)

class StylistAdmin(admin.ModelAdmin):
    list_display =('id','name','salon','email','phone_number')
    search_fields = ('salon',)
admin.site.register(Stylist,StylistAdmin)
