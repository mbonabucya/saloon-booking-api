from django.contrib import admin
from .models import *

# Register your models here.
#admin.site.register(Salon)
admin.site.register(Stylist)
admin.site.register(Booking)


class SalonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')
    search_fields = ('name',)

admin.site.register(Salon, SalonAdmin)
