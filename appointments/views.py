from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Appointment, AppointmentStatuse
from accounts.models import CustomUser
from .serializers import AppointmentListCreateSerializer, AppointmentSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAppointmentOwnerOrSecretary
from django.core.mail import send_mail
from django.conf import settings

class AppointmentList(ListCreateAPIView):
    serializer_class = AppointmentListCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        user = self.request.user
        if user.is_authenticated:
             if hasattr(user, 'role') and hasattr(user.role, 'role_name'):
                if user.role.role_name == 'Secretary':
                    return Appointment.objects.all()
                if user.role.role_name == 'Patient':
                    return Appointment.objects.filter(patient=user)
                elif user.role.role_name == 'Doctor':
                    return Appointment.objects.filter(doctor=user)
                else:
                    return Appointment.objects.none()

    def perform_create(self, serializer):
        user = self.request.user

        doctor_info = {}
        patient_info = {}
        confirmed_status = AppointmentStatuse.objects.get(status="Confirmed")

        if user.role.role_name == 'Doctor':
            doctor_info["id"] = user.id
            patient_info["id"] = serializer.validated_data.get('patient').id
            doctor_info["email"] = user.email
            patient_info["email"] = CustomUser.objects.get(id=patient_info["id"]).email
            doctor_info["full_name"] = f"{user.first_name} {user.last_name}"
            patient_info["full_name"] = f"{CustomUser.objects.get(id=patient_info['id']).first_name} {CustomUser.objects.get(id=patient_info['id']).last_name}"
            serializer.save(doctor=user, Appointment_status=confirmed_status)

        elif user.role.role_name == 'Patient':
            doctor_info["id"] = serializer.validated_data.get('doctor').id
            patient_info["id"] = user.id
            doctor_info["email"] = CustomUser.objects.get(id=doctor_info["id"]).email
            patient_info["email"] = user.email
            doctor_info["full_name"] = f"{CustomUser.objects.get(id=doctor_info['id']).first_name} {CustomUser.objects.get(id=doctor_info['id']).last_name}"
            patient_info["full_name"] = f"{user.first_name} {user.last_name}"
            serializer.save(patient=user, Appointment_status=confirmed_status)

        elif user.role.role_name == 'Secretary':
            doctor_info["id"] = serializer.validated_data.get('doctor').id
            patient_info["id"] = serializer.validated_data.get('patient').id
            doctor_info['email'] = CustomUser.objects.get(id=doctor_info["id"]).email
            patient_info["email"] = CustomUser.objects.get(id=patient_info["id"]).email
            doctor_info["full_name"] = f"{CustomUser.objects.get(id=doctor_info['id']).first_name} {CustomUser.objects.get(id=doctor_info['id']).last_name}"
            patient_info["full_name"] = f"{CustomUser.objects.get(id=patient_info['id']).first_name} {CustomUser.objects.get(id=patient_info['id']).last_name}"
            serializer.save(Appointment_status=confirmed_status)

        appointment_date = serializer.validated_data.get('Appointment_date')
        appointment_time = serializer.validated_data.get('Appointment_time')

        if "@" in patient_info["email"]:
            email_subject = 'EDental Clinic Appointment Confirmation'
            email_message = f'Thank you {patient_info["full_name"]} for booking an appointment!\n\n Your appointment is on {appointment_date} at {appointment_time} with doctor {doctor_info["full_name"]}.'
            recipient_email = patient_info["email"]
            send_mail(email_subject, email_message, settings.EMAIL_HOST_USER, [recipient_email], fail_silently=False)

        if "@" in doctor_info["email"]:
            email_subject = 'EDental Clinic New Appointment'
            email_message = f'Hello Doctor {doctor_info["full_name"]},\n\n You have a new appointment on {appointment_date} at {appointment_time} with patient {patient_info["full_name"]}.'
            recipient_email = doctor_info["email"]
            send_mail(email_subject, email_message, settings.EMAIL_HOST_USER, [recipient_email], fail_silently=False)



class AppointmentDetail(RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAppointmentOwnerOrSecretary, IsAuthenticated]





















# from rest_framework.generics import (
#     ListCreateAPIView,
#     RetrieveUpdateDestroyAPIView,
# )
# from .models import Appointment
# from .permissions import IsOwnerOrReadOnly, IsAppointmentsOwner
# from .serializers import AppointmentSerializer
# from rest_framework.permissions import IsAuthenticated


# class AppointmentList(ListCreateAPIView):
#     # if request.user.role:
#     # role_id = request.user.role
#     # role = UserRole.objects.filter(id = role_id)
#     queryset = Appointment.objects.filter()
#     serializer_class = AppointmentSerializer
#     permission_classes = [IsAppointmentsOwner, IsAuthenticated]
#     # print(request.user)

# class AppointmentDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Appointment.objects.all()
#     serializer_class = AppointmentSerializer
#     permission_classes = (IsOwnerOrReadOnly,)
