from django.contrib import admin
from django.contrib.auth.models import User
from .models import ScheduleModel, PlanModel


# Register your models here.
@admin.register(ScheduleModel)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ScheduleModel._meta.get_fields()]


@admin.register(PlanModel)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PlanModel._meta.get_fields()]
