from django.db import models
from django.db.models import Model, CharField, BooleanField, TextField, DateTimeField, OneToOneField
from django.contrib.auth.models import User
# Create your models here.


class Profile(Model):
    user = OneToOneField(User, on_delete=models.CASCADE)
    current_city = CharField(max_length=50)
    current_country = CharField(max_length=50)
    join_date = DateTimeField(auto_now_add=True)
