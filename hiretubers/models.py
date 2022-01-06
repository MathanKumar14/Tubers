from django.db import models
from datetime import datetime
# Create your models here.

class Hire(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    tuber_id = models.IntegerField(blank=True)
    user_id = models.IntegerField(blank=True)
    email = models.CharField(max_length=255)
    tuber_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.TextField(max_length=255)
    created_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.email