# Cite: https://www.youtube.com/watch?v=TBGRYkzXiTg

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
import datetime
from .models import Profile

from django.forms.widgets import Widget


# Creating this class to be able to add additional fields to the Sign Up form in signup.html
class SignUpForm(UserCreationForm):

    # Widgets are to create styling on the sign up form
    # Styling is from Bulma form styling documentation https://bulma.io/documentation/form/general/
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs= {'class': 'input is-success'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs= {'class': 'input is-success'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs= {'class': 'input is-success'}))
    current_city = forms.CharField(max_length=50, widget=forms.TextInput(attrs= {'class': 'input is-success'}))
    current_country = forms.CharField(max_length=50, widget=forms.TextInput(attrs= {'class': 'input is-success'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs= {'class': 'input is-success'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs= {'class': 'input is-success'}))
    date_joined  =datetime.datetime.now()

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name')

        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('current_city', 'current_country')