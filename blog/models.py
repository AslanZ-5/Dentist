from django.db import models
from datetime import datetime
from django.contrib.auth.admin import User


class Blog(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    posted = models.DateTimeField(default=datetime.now())
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
