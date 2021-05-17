from django.db import models
from django.db.models import Model, CharField, BooleanField, TextField, DateTimeField, OneToOneField, ForeignKey
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(Model):
    user = OneToOneField(User, on_delete=models.CASCADE)
    current_city = CharField(max_length=50)
    current_country = CharField(max_length=50)
    join_date = DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.user.username

class Post(Model):
    title = CharField(max_length=250)
    text = CharField(max_length=2000)
    image = CharField(max_length=500)
    user = ForeignKey(User, default=1, null=True, on_delete=models.CASCADE)

def __str__(self):
    return self.title
         
    

class City(Model):
    name = CharField(max_length=50)
    country = CharField(max_length=50)
    image_thumbnail = CharField(max_length=500)
    image_detailed = CharField(max_length=500)

    def __str__(self):
        return self.name


