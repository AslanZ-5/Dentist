from django.urls import path
from .views import AppointmentsView,AppointmentListView

app_name = 'appointments'


urlpatterns = [
   path('',AppointmentsView,name='appointments'),
   path('your_appointments/',AppointmentListView.as_view(),name='your_appointments'),

]