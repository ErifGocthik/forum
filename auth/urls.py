from django.contrib.auth.views import LoginView
from django.urls import path

app_name = 'custom_auth'

urlpatterns = [
    path('sign-in/', LoginView.as_view(template_name='auth/sign-in.html'), name='sign-in'),
]
