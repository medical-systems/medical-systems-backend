from django.contrib import admin
from .models import Appointment, AppointmentStatuse

# Register your models here.
admin.site.register(Appointment)
admin.site.register(AppointmentStatuse)
