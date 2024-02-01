from django.urls import path
from . import views

urlpatterns = [
    path("schedule/<int:schedule_id>", views.get_schedule),
    path("schedules", views.get_schedules),
    path("plans", views.get_plans, name="plans"),
    path("delete_plan/<str:plan_id>/", views.delete_plan),
    path("delete_plans", views.delete_plans),
]
