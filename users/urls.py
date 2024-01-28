from django.urls import path
from allauth.account.views import LoginView
from . import views

urlpatterns = [
    path("logout/", views.logout_view),
    path("", views.home),
]
