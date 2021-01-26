from django.shortcuts import render, redirect
from .forms import AppointCreationForm
from django.views.generic import (CreateView, ListView)
from .models import Appointments
from django.core.mail import send_mail


# class AppointmentsView(CreateView):
#     model = Appointments
#     fields = ['name', 'phone', 'email', 'location', 'date', 'time', 'text']
#     template_name = 'appointments/appointments.html'
#
#     def message1(self,request):
#         message = {
#             "name":request.POST['name'],
#             'phone':request.POST["phone"],
#             'email':request.POST["email"],
#             'location':request.POST["location"],
#             'date':request.POST["date"],
#             'time':request.POST["time"],
#             'text':request.POST["text"],
#         }
#         return message
#
#     send_mail(
#         f'New Appointment',
#         message1(request=),
#         'zurabov.96@mail.ru',
#         ['asl.zurabov@gmail.com'],
#         fail_silently=False
#     )
#
#     def form_valid(self, form):
#         form.instance.account = self.request.user
#         return super().form_valid(form)

def AppointmentsView(request):
    if request.method == 'POST':
        form = AppointCreationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.account = request.user

            send_mail(
                'New Appointment',
                f'{form.instance.name},\n{form.instance.phone},\n{form.instance.email},\n{form.instance.location},\n{form.instance.date},\n{form.instance.time},\n{form.instance.text}',
                'zurabov.96@mail.ru',
                ['asl.zurabov@gmail.com'],
                fail_silently=False
            )
            instance.save()
            return redirect(instance.get_absolute_url())
    else:
        form = AppointCreationForm()
    return render(request,  'appointments/appointments.html', {'form': form})


class AppointmentListView(ListView):
    model = Appointments
    template_name = 'appointments/appointments_list.html'
    context_object_name = 'objects'
