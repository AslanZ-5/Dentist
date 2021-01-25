from django.db import models


class Price(models.Model):
    title = models.CharField(max_length=50)
    stage = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0)

    def __str__(self):
        return self.title

