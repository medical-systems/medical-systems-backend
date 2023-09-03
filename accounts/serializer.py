from rest_framework import serializers
from .models import CustomUser, UserRole, UserInsurance, UserGender
from appointments.models import AppointmentStatuse
from django.contrib.auth import get_user_model


class AllUserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "first_name", "last_name", "username", "email", "phone_num", "date_of_birth", "gender", "role", "insurance"]


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "photo", "first_name", "last_name", "username", "email", "phone_num", "date_of_birth", "gender", "role", "insurance"]


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("username", "email", "password", "confirm_password", "role")

    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop("confirm_password", None)

        patient_role = UserRole.objects.get(role_name='Patient')

        user = get_user_model().objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            role=patient_role,
        )
        return user


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGender
        fields = ["gender"]

class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInsurance
        fields = ["insurance_name"]

class AppointmentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentStatuse
        fields = ["status"]
