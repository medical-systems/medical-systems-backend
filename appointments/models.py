from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from accounts.models import CustomUser

class AppointmentStatuse(models.Model):
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.status


class Treatment(models.Model):
    treatment_name = models.CharField(max_length=255, blank=True, default=" ")

    def __str__(self):
        return self.treatment_name

class Appointment(models.Model):

    Appointment_date = models.DateField(null=True)
    Appointment_time = models.TimeField(null=True)
    Appointment_status = models.ForeignKey(AppointmentStatuse, on_delete=models.SET_NULL, null=True)
    notes = models.CharField(max_length=255, default="empty", blank=True, null=True)
    payment = models.IntegerField(default=0, blank=True)
    treatment = models.ForeignKey(Treatment, on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='doctor_appointments',
        limit_choices_to={'role__role_name': 'Doctor'})
    patient = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='patient_appointments',
        limit_choices_to={'role__role_name': 'Patient'})

    def __str__(self):
        return f"Appointment for patient {self.patient}, with doctor {self.doctor}"

    def get_absolute_url(self):
        return reverse('appointment_detail', args=[str(self.id)])

