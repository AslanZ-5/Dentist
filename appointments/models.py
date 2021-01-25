from django.db import models
from django.urls import reverse
from django.contrib.auth.admin import User


class Appointments(models.Model):
    class PrefLocation(models.TextChoices):
        NAZRAN = 'NAZRAN'
        MALGOBEK = 'MALGOBEK'
        KARBULAK = 'KARBULAK'
        SUNZA = 'SUNZA'
        MAGAS = 'MAGAS'

    preffered_time = [('Morning', 'Morning'),
                      ('Afternoon', 'Afternoon'),
                      ('Evening', 'Evening')
                      ]
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    location = models.CharField(max_length=50, choices=PrefLocation.choices)
    date = models.DateField()
    time = models.CharField(choices=preffered_time, max_length=50)
    text = models.TextField()
    account = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('website:home')
