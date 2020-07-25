from django.db import models,migrations

# Create your database models here.
class Flight(models.Model):
    origin=models.CharField(max_length=80)
    destination=models.CharField(max_length=80)
    duration = models.IntegerField()