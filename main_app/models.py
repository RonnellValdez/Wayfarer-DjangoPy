from django.db import models
from django.db.models import Model, CharField, BooleanField, TextField, DateTimeField

# Create your models here.

class User(Model):

    name = CharField(max_length=100)
    currentLocation = CharField(max_length=500)
    join_date = DateTimeField(auto_now_add=True)