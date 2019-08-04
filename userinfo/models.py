from django.conf import settings
from django.db import models
from django.utils import timezone


class User(models.Model):
    phoneNo = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title