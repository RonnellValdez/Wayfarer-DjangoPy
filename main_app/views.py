from main_app.forms import SignUpForm
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from .forms import SignUpForm, ProfileForm

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

class Profile(TemplateView):
    template_name = 'profile.html'

class Signup(View):
    def get(self, request):
        form = SignUpForm()
        context = {'form': form}
        return render(request, "registration/signup.html", context)


    def post(self, request):
        form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            user.Profile = profile_form.save()
            login(request, user)
            return redirect("home")
        else:
            context = {"form": form,
                        "profile": profile_form}
            return render(request, "registration/signup.html", context)