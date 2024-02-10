from django.db import models
from django.db.models import Index
from django.db.models.functions import Upper
from django.contrib.auth.models import User


# Create your models here.
class ScheduleModel(models.Model):
    uuid = models.TextField("uuid", max_length=32, unique=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    schedule_name = models.CharField("schedule_name", max_length=50)
    schedule_info = models.TextField("schedule_info", max_length=500)
    created_time = models.TextField("created_time", max_length=10)

    class Meta:
        db_table = "schedule"


class PlanModel(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.TextField("plan")

    class Meta:
        db_table = "plan"
