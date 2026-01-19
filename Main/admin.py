from django.contrib import admin
from .models import Appointment

# Register your models here.

# admin.site.register(contact.html)




@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'doctor', 'appointment_date')
    list_filter = ('department', 'doctor', 'appointment_date')
    search_fields = ('name', 'email', 'phone')
