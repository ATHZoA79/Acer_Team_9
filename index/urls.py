from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("scenic/", views.scenic),
    re_path(r"^search/$", views.search),
]
