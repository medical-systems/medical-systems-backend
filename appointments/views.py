from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Appointment
from .permissions import IsOwnerOrReadOnly
from .serializers import AppointmentSerializer

from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail



from rest_framework.response import Response
from rest_framework import status


class AppointmentList(ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        email=self.request.user.email
        username=self.request.user.username



        send_mail(
            'Appointment Confirmation',
            f'{username} ,Thank you for booking an appointment! ',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class AppointmentDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer






