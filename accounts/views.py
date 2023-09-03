from django.urls import reverse_lazy
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .models import CustomUser, UserInsurance, UserGender, UserRole
from appointments.models import AppointmentStatuse, Treatment
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializer import UserInfoSerializer, AllUserInfoSerializer, CustomUserSerializer, GenderSerializer, InsuranceSerializer, AppointmentStatusSerializer, TreatmentSerializer, DoctorListSerializer, PatientListSerializer
from .permissions import IsAccountOwnerOrSecretary
from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class SignUpView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountListView(ListAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = AllUserInfoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        user = self.request.user
        if user.is_authenticated and hasattr(user, 'role') and hasattr(user.role, 'role_name'):
            if user.role.role_name == 'Secretary':
                return CustomUser.objects.all()

            else:
                return CustomUser.objects.none()


class AccountDetail(RetrieveUpdateDestroyAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = UserInfoSerializer
    permission_classes = [IsAccountOwnerOrSecretary, IsAuthenticated]


class DoctorListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = DoctorListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        user = self.request.user
        if user.is_authenticated and hasattr(user, 'role') and hasattr(user.role, 'role_name'):
            return CustomUser.objects.filter(role=UserRole.objects.get(role_name="Doctor"))
        else:
            return CustomUser.objects.none()


class PatientListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = PatientListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        user = self.request.user
        if user.is_authenticated and hasattr(user, 'role') and hasattr(user.role, 'role_name'):
            if user.role.role_name == 'Secretary' or user.role.role_name == 'Doctor':
                return CustomUser.objects.filter(role=UserRole.objects.get(role_name="Patient"))
            else:
                return CustomUser.objects.none()


class StaticTablesInfoView(APIView):

    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        all_genders = UserGender.objects.all()
        all_insurances = UserInsurance.objects.all()
        all_appointment_statuses = AppointmentStatuse.objects.all()
        all_treatments = Treatment.objects.all()

        gender_serializer = GenderSerializer(all_genders, many = True)
        insurance_serializer = InsuranceSerializer(all_insurances, many = True)
        appointment_status_serializer = AppointmentStatusSerializer(all_appointment_statuses, many = True)
        treatment_serializer = TreatmentSerializer(all_treatments, many = True)


        response_data = {
                "genders": gender_serializer.data,
                "insurances": insurance_serializer.data,
                "appointment_statuses": appointment_status_serializer.data,
                "treatments": treatment_serializer.data,
            }

        return Response(response_data)
