from rest_framework import serializers
from .models import Appointment
from accounts.models import CustomUser

class AppointmentListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"

    def create(self, validated_data):
        return super().create(validated_data)
