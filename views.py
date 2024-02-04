from django.shortcuts import render
from .models import ScheduleModel, PlanModel
import time
import openai


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
    # 為了測試加的,可以再改
    schdule_name = "澎湖行"
    splans = {schdule_name:["King飛鏢酒吧" ,"澎湖仙人掌冰城" ,"真鮮味小吃部" ,"日立大飯店", "西嶼彈藥本庫軍事文化園區","山水吼洞"]}
    return splans
    # 為了測試加的,可以再改

#################################################################################
#                                  OpenAI API 產生行程表
#################################################################################
"""
"uuid",(行程表編號，避免行程表名稱相同時互相覆蓋)
"username",
"schdule_name",(行程表名稱，可重複但不建議)
"schedule_info",(行程內容)
"created_time",(行程表建立時間，輔助使用者辨識)
"""
def travel_itinerary_to_str(scenic=""):#(行程內容) schedule_info   

    openai.api_key = "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"

    scenic = '''請幫我安排一個包含'''+scenic+'''的行程,以一個list的dict格式顯示，dict內部有location和time兩個key分別代表地點和時間，
    時間以範圍表示，
    例如:[
    {"location": "國立故宮博物院", "time": "10:00~13:00"},
    {"location": "中正紀念堂", "time": "13:30~15:00"}   
    ]，不需要前後文。'''
    
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo", 
      messages=[{"role": "user", "content": scenic}])
    
    schedule_info = completion.choices[0].message.content
    
    #按時間排序
    schedule_info = eval(schedule_info)
   
    def get_time(f):
      return f["time"]

    schedule_info.sort(key=get_time)
    schedule_info = str(schedule_info)
    #按時間排序
    return schedule_info

def schedule_created_time():#行程表建立時間,格式是yyyymmddhhmmss created_time
    t = time.time()
    t = time.localtime(t)
    #print(t)
    s = ""
    s += str(t.tm_year)
    s += str(t.tm_mon).zfill(2)
    s += str(t.tm_mday).zfill(2)
    s += str(t.tm_hour).zfill(2)
    s += str(t.tm_min).zfill(2)
    s += str(t.tm_sec).zfill(2)
    return s

def time_to_uuid(date = "20240204210931"):# uuid = ****** uuid",(行程表編號，避免行程表名稱相同時互相覆蓋)
    time_int = int(date)
    uuid_number = int(time_int / 1000000) + time_int % 1000000
    uuid_number = uuid_number % 1000000 #將日期轉換成6位編碼
    #print(uuid_number)
    uuid = str(uuid_number).zfill(6)#如果不足6碼,前面補0
    
    return uuid

def generate_schedule(request):
    """用 OpenAI API 產生行程表"""
    try:
        username = request.user.id
    except:
        print("username don't found")
        return
    
    try:
        splans = save_plan(request)
        schdule_name = list(splans.keys())[0]
    except:
        print("Plans don't svae")
        return
    
    try:
        scenic = ""
        for sp in splans[schdule_name]:
            scenic += ","+sp
        schedule_info = travel_itinerary_to_str(scenic)
    except:
        print("Plans don't svae")
        return
    
    try:
        created_time = schedule_created_time()
    except:
        print("created_time isn't created")
        return
    
    try:
        uuid = time_to_uuid(created_time)
    except:
        print("uuid isn't done well")
        return
    
    return uuid,username,schdule_name,schedule_info,created_time

#################################################################################
#                           OpenAI API 產生行程表
#################################################################################


def delete_plan(username):
    """儲存行程表之後刪除關注清單"""
    pass

#ScheduleModel(uuid, username, schedule)