from statistics import mode
from django.db import models

# Create your models here.
class Records(models.Model):
    username = models.CharField()
    date = models.DateField(auto_now_add=True, null=False)
    clockInTime = models.TimeField(auto_now_add=True, null=False)
    clockOutTime = models.TimeField(auto_now_add=True, null=False)
    status = models.BooleanField()
    totalTime = models.DurationField()
    