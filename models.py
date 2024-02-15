from django.db import models
from django.db.models import Index
from django.db.models.functions import Upper
from django.contrib.auth.models import User


# Create your models here.
class ScheduleModel(models.Model):
    uuid = models.TextField("uuid", max_length=36, unique=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    schedule_name = models.CharField("schedule_name")#行程表名稱，可當標題
    schedule_info = models.TextField("schedule_info")#行程內容
    created_time = models.TextField("created_time")#行程表建立時間

    class Meta:
        db_table = "schedule"

"""
"uuid",(行程表編號，避免行程表名稱相同時互相覆蓋)
"username",
"schdule_name",(行程表名稱，可重複但不建議)
"schedule_info",(行程內容)
"created_time",(行程表建立時間，輔助使用者辨識)
"""


class PlanModel(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.TextField("plan")

    class Meta:
        db_table = "plan"
