# Cite: https://www.youtube.com/watch?v=TBGRYkzXiTg

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
import datetime


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    current_city = forms.CharField(max_length=50)
    current_country = forms.CharField(max_length=50)
    date_joined  =datetime.datetime.now()

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name')
    