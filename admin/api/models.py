from django.db import models

# Create your models here.
from datetime import datetime


class Room(models.Model):
    name = models.CharField(max_length=1000)

    objects = models.Manager()


class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)

    objects = models.Manager()
