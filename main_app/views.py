from main_app.forms import SignUpForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from .forms import SignUpForm, ProfileForm
from django.http import HttpResponse


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile
# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

# @method_decorator(login_required, name='dispatch')
class ProfileDetail(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.get(user=self.request.user)
        return context

    

class Signup(View):
    def get(self, request):
        form = SignUpForm()
        context = {'form': form}
        return render(request, "registration/signup.html", context)

# CITE: https://stackoverflow.com/questions/57918725/how-to-extend-django-usercreationform-model-to-include-phone-number-field
    def post(self, request):
        form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid(): 
            user = form.save()
            profile_form = profile_form.save(commit=False)
            profile_form.user = user
            profile_form.save()
            login(request, user)
            return redirect("profile")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

@method_decorator(login_required, name='dispatch')

class UpdateUser(UpdateView):
    model = User
    fields = ['first_name']
    template_name = "user_update.html"
    success_url = '/profile/'

    # def get_success_url(self):
    #     return reverse('profile', kwargs={'pk': self.object.pk})

class UpdateProfile(UpdateView):
    model = Profile
    fields = ['current_city']
    template_name = "profile_update.html"
    success_url = '/profile/'

    # def get_success_url(self):
    #     return reverse('profile', kwargs={'pk': self.object.pk})