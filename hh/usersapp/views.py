from django.contrib.auth.views import LoginView
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from .models import HhUser
from .forms import RegForm


class RegCreateView(CreateView):
    model = HhUser
    template_name = 'usersapp/reg.html'
    form_class = RegForm
    success_url = reverse_lazy('users:login')


class UserLoginView(LoginView):
    template_name = 'usersapp/login.html'


class UserDetailView(DetailView):
    model = HhUser
    template_name = 'usersapp/profile.html'
