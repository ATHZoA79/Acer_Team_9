from django.db import models
from django.db.models import Index
from django.db.models.functions import Upper
from django.contrib.auth.models import User


# Create your models here.
class ScheduleModel(models.Model):
    uuid = models.TextField("uuid", max_length=36, unique=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    schedule = models.TextField("schedule")

    class Meta:
        db_table = "schedule"


class PlanModel(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.TextField("plan")

    class Meta:
        db_table = "plan"
