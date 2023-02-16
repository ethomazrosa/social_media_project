from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms

# Views
class SignUp(CreateView):
    form_class = forms.SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


