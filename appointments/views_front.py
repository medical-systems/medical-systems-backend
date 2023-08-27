from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Appointment


class AppointmentListView(LoginRequiredMixin, ListView):
    template_name = "appointments/appointment_list.html"
    model = Appointment
    context_object_name = "appointments"


class AppointmentDetailView(LoginRequiredMixin, DetailView):
    template_name = "appointments/appointment_detail.html"
    model = Appointment


class AppointmentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "appointments/appointment_update.html"
    model = Appointment
    fields = "__all__"


class AppointmentCreateView(LoginRequiredMixin, CreateView):
    template_name = "appointments/appointment_create.html"
    model = Appointment
    fields = ["name", "rating", "reviewer"] # "__all__" for all of them


class AppointmentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "appointments/appointment_delete.html"
    model = Appointment
    success_url = reverse_lazy("appointment_list")
