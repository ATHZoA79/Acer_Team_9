from django.urls import path
from . import views

urlpatterns = [
    path("delete_schedule/<str:schedule_uuid>/", views.delete_schedule),
    path("schedules/", views.schedule_view, name="schedules"),
    path("plans/", views.plans_view, name="plans"),
    path("add_plan/", views.add_plan),
    path("delete_plan/<str:plan_id>/", views.delete_plan),
    # path("delete_plans/", views.test_delete_plans),
    path("save_plan/", views.generate_schedule),
]
