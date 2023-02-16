from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.urls import reverse
from django.views.generic import (CreateView, DetailView,
                          ListView)
from .models import Group, GroupMember

# Views
class CreateGroup(LoginRequiredMixin, CreateView):
    model = Group
    fields = ('name', 'description')


class SingleGroup(DetailView):
    model = Group


class ListGroup(ListView):
    model = Group