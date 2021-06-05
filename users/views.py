from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterView(CreateView):
    template_name = "users/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('profile')


class ProfileView(DetailView):
    template_name = "users/profile.html"
    model = User
    context_object_name = "User"


        
    
