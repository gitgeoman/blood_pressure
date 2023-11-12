from django.db import models

# Create your models here.

class Measurement(models.Model):
    date = models.DateTimeField()
    diastolic = models.IntegerField()
    systolic = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)