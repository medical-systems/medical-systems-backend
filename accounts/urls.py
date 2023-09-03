from django.urls import path

from .views import SignUpView, AccountDetail, AccountListView, PatientListView, DoctorListView

urlpatterns = [
    path("", AccountListView.as_view(), name="account_list"),
    path("doctors/", DoctorListView.as_view(), name="doctor_list"),
    path("patients/", PatientListView.as_view(), name="patient_list"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("<int:pk>/", AccountDetail.as_view(), name="acoount_datail"),

]
