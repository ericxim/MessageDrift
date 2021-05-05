from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterView(CreateView):
    template_name = "users/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('profile')

class ProfileView(ListView):
    template_name = "users/profile.html"
    def get_queryset(self):
        self.profile = get_object_or_404(User, username=self.kwargs['name'])

        
    
