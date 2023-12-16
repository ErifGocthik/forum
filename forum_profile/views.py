from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from forum_profile.forms import ProfileCreationForm
from forum_profile.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    template_name = 'forum_profile/profile_form.html'
    success_url = reverse_lazy('profile:profile_create')