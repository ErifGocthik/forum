from django.urls import path

from forum_profile.views import ProfileCreateView

app_name = 'forum_profile'

urlpatterns = [
    path('create_profile/', ProfileCreateView.as_view(), name='profile_create'),
]