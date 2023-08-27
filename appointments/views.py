from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Appointment
from .permissions import IsOwnerOrReadOnly
from .serializers import AppointmentSerializer


class AppointmentList(ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class AppointmentDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
