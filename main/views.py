from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import ScheduleModel, PlanModel


# Create your views here.
def get_schedules(request):
    """取得用戶所有行程表，顯示在用戶首頁上"""
    pass


def get_schedule(request):
    """取得單一行程表"""
    pass


def save_plan_to_scedule(request):
    """將關注清單儲存成行程表"""
    pass


def generate_schedule(request):
    """用 OpenAI API 產生行程表"""
    pass


def get_plans(request):
    """取得所有關注行程並傳送到前端頁面"""
    user = request.user
    plans = PlanModel.objects.filter(username=user.id).all()
    if request.method == "POST":
        title = request.POST.get("title", "")

        # 取得所有 'plan' 欄位的值
        plans = request.POST.getlist("plan")
        content = {"title": title, "plans": plans}

        # 進行進一步的處理，例如儲存到資料庫等操作
        # ...

        return render(request, "main/test.html", content)
    content = {"plans": plans}
    return render(request, "main/plan.html", context=content)


def delete_plan(request, plan_id):
    """在確認儲存成行程表之前，刪除單一個關注行程"""
    if request.method == "POST":
        try:
            plan_to_delete = PlanModel.objects.get(id=eval(plan_id))
            plan_to_delete.delete()
            return HttpResponse("Plan deleted successfully!")
        except PlanModel.DoesNotExist:
            return HttpResponse("Plan does not exist.")

    return HttpResponse("Invalid request.")


def delete_plans(request):
    """儲存行程表之後刪除關注清單"""
    pass
