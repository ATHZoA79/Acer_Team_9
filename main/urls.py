from django.urls import path
from . import views
from .decorators import login_required_decorator

urlpatterns = [
    path("delete_schedule/", views.delete_schedule),
    path("schedules/", login_required_decorator(views.schedule_view), name="schedules"),
    path("plans/", login_required_decorator(views.plans_view), name="plans"),
    path("add_plan/", login_required_decorator(views.add_plan)),
    path("delete_plan/<str:plan_id>/", views.delete_plan),
    # path("delete_plans/", views.test_delete_plans),
    path("save_plan/", login_required_decorator(views.generate_schedule)),
]
