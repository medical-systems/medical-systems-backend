from django.contrib import admin
from .models import Appointment, AppointmentStatuse,Treatments,AppointmentTreatment

# Register your models here.
admin.site.register(Appointment)
admin.site.register(AppointmentStatuse)
admin.site.register(AppointmentTreatment)
admin.site.register(Treatments)

