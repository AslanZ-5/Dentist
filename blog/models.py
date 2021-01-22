from django.db import models
from datetime import datetime
from django.contrib.auth.admin import User
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    posted = models.DateTimeField(default=datetime.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        a = self.text
        return a[:180] + ' ...' if len(a) > 180 else a[:180]

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
