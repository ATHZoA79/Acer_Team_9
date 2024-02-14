from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, HttpResponseServerError, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import ScheduleModel, PlanModel
import openai
from datetime import datetime
import json
import os
from uuid import uuid4


# Create your views here.
def schedule_view(request):
    """取得用戶所有行程表，顯示在用戶首頁上"""
    user_id = request.user.id
    schedules = ScheduleModel.objects.filter(username_id=user_id).all()
    schedules = [model_to_dict(schedule) for schedule in schedules]

    for schedule in schedules:
        # 將字串解析成pyhton的json串列
        schedule["schedule_info"] = schedule["schedule_info"].replace("'", '"')
        schedule["schedule_info"] = json.loads(schedule["schedule_info"])

        # 轉換時間格式
        schedule["created_time"] = datetime.utcfromtimestamp(
            eval(schedule["created_time"])
        ).strftime("%Y-%m-%d %H:%M:%S")

    response = {"schedules": schedules}
    return render(request, "main/schedule.html", response)


@csrf_exempt
def delete_schedule(request: HttpRequest):
    """刪除行程表"""
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            uuid = data["schedule_uuid"]
            print(uuid)
            schedule_to_delete = ScheduleModel.objects.get(uuid=uuid)
            schedule_to_delete.delete()
            return HttpResponse("Schedule Delete Successfully.")
        except ScheduleModel.DoesNotExist:
            return HttpResponse("Schedule does not exist.")
    return HttpResponse("Invalid request.")


def save_plan(request):
    """將關注清單儲存成行程表"""
    # 為了測試加的,可以再改
    schdule_name = "澎湖行"
    splans = {
        schdule_name: [
            "King飛鏢酒吧",
            "澎湖仙人掌冰城",
            "真鮮味小吃部",
            "日立大飯店",
            "西嶼彈藥本庫軍事文化園區",
            "山水吼洞",
        ]
    }
    return splans


def travel_itinerary_to_str(scenic=""):  # (行程內容) schedule_info
    """將提詞(prompt)傳送到OpenAPI取得回覆"""
    api_key = os.environ.get("OPENAI_API")

    scenic = (
        """請幫我安排一個包含"""
        + scenic
        + """的行程,以一個list的dict格式顯示，dict內部有location和time兩個key分別代表地點和時間，
    時間以範圍表示，
    例如:[
    {"location": "國立故宮博物院", "time": "10:00~13:00"},
    {"location": "中正紀念堂", "time": "13:30~15:00"}   
    ]，不需要前後文和以上範例資訊。"""
    )
    completion = openai.OpenAI(api_key=api_key).chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": scenic,
            },
        ],
    )
    # completion = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo", messages=[{"role": "user", "content": scenic}]
    # )
    schedule_info = completion.choices[0].message.content
    # 按時間排序
    schedule_info = eval(schedule_info)

    def get_time(f):
        return f["time"]

    schedule_info.sort(key=get_time)
    schedule_info = str(schedule_info)
    # 按時間排序
    return schedule_info


def schedule_created_time():
    """產生Unix時間戳(以秒計算，共十位數)"""
    unix_timestamp = (datetime.utcnow() - datetime(1970, 1, 1)).total_seconds()
    timestamp = int(unix_timestamp)
    return timestamp


def time_to_uuid(
    date="20240204210931",
):  # uuid = ****** uuid",(行程表編號，避免行程表名稱相同時互相覆蓋)
    time_int = int(date)
    uuid_number = int(time_int / 1000000) + time_int % 1000000
    uuid_number = uuid_number % 1000000  # 將日期轉換成6位編碼
    # print(uuid_number)
    uuid = str(uuid_number).zfill(6)  # 如果不足6碼,前面補0

    return uuid


def generate_schedule(request):
    """用 OpenAI API 產生行程表"""
    try:
        user_id = request.user.id
    except:
        print("username don't found")
        return HttpResponse("username don't found")

    try:
        splans = save_plan()
        schedule_name = list(splans.keys())[0]
    except:
        print("Plans don't svae")
        return HttpResponse("Plans don't save")

    try:
        scenic = ""
        for sp in splans[schedule_name]:
            scenic += "," + sp
        schedule_info = travel_itinerary_to_str(scenic)
    except:
        print("Plans don't svae")
        return HttpResponse("Plans don't save")
    # try:
    #     scenic = ""
    #     plans = get_plans()
    #     for p in plans:
    #         scenic += "," + p
    #     schedule_info = travel_itinerary_to_str(scenic)
    # except:
    #     print("Plans don't svae")
    #     return HttpResponse("Plans don't save")

    try:
        created_time = schedule_created_time()
    except:
        print("created_time isn't created")
        return HttpResponse("created_time isn't created")

    try:
        uuid = time_to_uuid(created_time)
    except:
        print("uuid isn't done well")
        return HttpResponse("uuid isn't done well")

    schedule_to_save = ScheduleModel(
        uuid=uuid,
        username_id=user_id,
        schedule_name=schedule_name,
        schedule_info=schedule_info,
        created_time=created_time,
    )
    schedule_to_save.save()
    response = {
        "uuid": uuid,
        "username_id": user_id,
        "schedule_name": schedule_name,
        "schedule_info": schedule_info,
        "created_time": created_time,
    }
    return render(request, "main/save_plan.html", response)


@csrf_exempt
def add_plan(request: HttpRequest):
    """將單一個地點加入關注清單"""
    if request.method == "POST":
        try:
            user_id = request.user.id
            data = json.loads(request.body)
            # return JsonResponse(data)
            # plan = data["plan"]
            # return HttpResponse(plan)
            plan_to_add = PlanModel()
            plan_to_add.username_id = user_id
            plan_to_add.plan = data["plan"]
            plan_to_add.save()
            # return HttpResponse(f"{plan} is added to plan list.")
            response_data = {"message": "Success"}
            return JsonResponse(response_data)
        except:
            return HttpResponseServerError("Error on adding plan")


def plans_view(request: HttpRequest):
    """取得所有關注行程並傳送到前端頁面"""
    user_id = request.user.id
    plans = PlanModel.objects.filter(username=user_id).all()
    if request.method == "POST":
        title = request.POST.get("title", "")

        # 取得所有 'plan' 欄位的值
        plans = request.POST.getlist("plan")
        prompt_str = ",".join(plans)
        schedule_info = travel_itinerary_to_str(prompt_str)
        unix_timestamp = int((datetime.utcnow() - datetime(1970, 1, 1)).total_seconds())
        schedule_to_save = ScheduleModel(
            uuid=str(uuid4()),
            username_id=user_id,
            schedule_name=title,
            schedule_info=schedule_info,
            created_time=unix_timestamp,
        )
        schedule_to_save.save()
        result = delete_plans(user_id)
        if result:
            return redirect("schedules")
        else:
            return HttpResponse("Schedule Save Error.")
        # response = {
        #     "uuid": str(uuid4()),
        #     "title": title,
        #     "plans": plans,
        #     "schedule_info": schedule_info,
        #     "created_at": unix_timestamp,
        # }

        # return render(request, "main/test.html", response)
    response = {"plans": plans}
    return render(request, "main/plans.html", response)


def get_plans(request: HttpRequest):
    """內部程式調用，回傳包含景點名稱的list"""
    user_id = request.user.id
    plans = PlanModel.objects.filter(username=user_id).all()
    plans = [plan.plan for plan in plans]
    return plans


@csrf_exempt
def delete_plan(request: HttpRequest, plan_id):
    """在確認儲存成行程表之前，刪除單一個關注行程"""
    if request.method == "POST":
        try:
            plan_to_delete = PlanModel.objects.get(id=eval(plan_id))
            plan_to_delete.delete()
            return HttpResponse("Plan deleted successfully!")
        except PlanModel.DoesNotExist:
            return HttpResponse("Plan does not exist.")
    return HttpResponse("Invalid request.")


@csrf_exempt
def test_delete_plans(request: HttpRequest):
    """儲存行程表之後刪除關注清單<<Postman測試用>>"""
    if request.method == "POST":
        try:
            user = request.user
            plans = PlanModel.objects.filter(username=user.id).all()
            plans.delete()
            return HttpResponse("All plans deleted successfully.")
        except:
            return HttpResponse("Error on delete plans.")


def delete_plans(user_id):
    """儲存行程表之後刪除關注清單<<內部程式呼叫用>>"""
    try:
        plans = PlanModel.objects.filter(username=user_id).all()
        plans.delete()
        return True
    except:
        return False
