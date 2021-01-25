from django.shortcuts import render

from django.views.generic import (CreateView,ListView)
from .models import Appointments


class AppointmentsView(CreateView):
    model = Appointments
    fields = ['name', 'phone', 'email', 'location', 'date', 'time', 'text']
    template_name = 'appointments/appointments.html'

    def form_valid(self, form):
        form.instance.account = self.request.user
        return super().form_valid(form)


class AppointmentListView(ListView):
    model = Appointments
    template_name =  'appointments/appointments_list.html'
    context_object_name = 'objects'





