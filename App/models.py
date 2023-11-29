from django.db import models

# Create your models here.

class Client(models.Model):
    fname = models.CharField(max_length=20, blank=False)
    lname = models.CharField(max_length=20, blank=False)
    email = models.EmailField()
    message = models.TextField(default="decsription")

    def __str__ (self):
        return self.lname


class Trip(models.Model):
    pickup = models.CharField(max_length=10)
    dropoff = models.CharField(max_length=20)
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return self.pickup