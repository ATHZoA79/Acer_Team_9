from django.shortcuts import render
from .models import ScheduleModel, PlanModel


# Create your views here.
def index(request):
    return render(request, "index.html")


def get_schedules(request):
    """取得用戶所有行程表"""
    pass


def get_schedule(request):
    """取得單一行程表"""
    pass


def save_plan(request):
    """將關注清單儲存成行程表"""
    pass


def generate_schedule(request):
    """用 OpenAI API 產生行程表"""
    pass


def delete_plan(username):
    """儲存行程表之後刪除關注清單"""
    pass
