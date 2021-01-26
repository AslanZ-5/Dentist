from django.forms import ModelForm
from .models import Appointments
## This if you use function in views.py, else you don't need this
class AppointCreationForm(ModelForm):
    class Meta:
        model = Appointments
        fields = ['name', 'phone', 'email', 'location', 'date', 'time', 'text']
