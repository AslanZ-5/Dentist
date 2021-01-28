from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profileIMG')

    def __str__(self):
        return self.user.username

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height >300 or img.width > 300:
            output = (300,300)
            img.thumbnail(output)
            img.save(self.image.path)