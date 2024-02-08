from django.http import HttpResponse, HttpRequest
from django.forms.models import model_to_dict
from django.shortcuts import render, redirect
from init_db.models import (
    FoodModel,
    DrinkModel,
    HotelModel,
    RestaurantModel,
    BarModel,
    SightModel,
)


# Create your views here.
def index(request: HttpRequest):
    return render(request, "index.html")


def scenic(request: HttpRequest):
    return render(request, "scenic.html")


def search(request: HttpRequest):
    page = request.GET.get("page", 1)
    page = eval(page)
    per_page = request.GET.get("per_page", 10)
    per_page = eval(per_page)
    region = request.GET.get("region", "")
    genre = request.GET.get("genre", "food")
    offset = (page - 1) * per_page
    GROUP_LIMIT = 5
    if genre == "food":
        food_data = FoodModel.objects.filter(region=region).all()
        drink_data = DrinkModel.objects.filter(region=region).all()
        page_limit = len(food_data + drink_data) // per_page + 1
        food_data = [
            model_to_dict(item) for item in food_data[offset : offset + GROUP_LIMIT]
        ]
        drink_data = [
            model_to_dict(item) for item in drink_data[offset : offset + GROUP_LIMIT]
        ]
        datas = food_data + drink_data
    if genre == "hotel":
        datas = HotelModel.objects.filter(region=region).all()
        page_limit = len(datas) // per_page + 1
        datas = [model_to_dict(item) for item in datas[offset : offset + per_page]]
    if genre == "bar":
        datas = BarModel.objects.filter(region=region).all()
        page_limit = len(datas) // per_page + 1
        datas = [model_to_dict(item) for item in datas[offset : offset + per_page]]
    if genre == "sight":
        datas = SightModel.objects.filter(region=region).all()
        page_limit = len(datas) // per_page + 1
        datas = [model_to_dict(item) for item in datas[offset : offset + per_page]]
    if genre == "restaurant":
        datas = RestaurantModel.objects.filter(region=region).all()
        page_limit = len(datas) // per_page + 1
        datas = [model_to_dict(item) for item in datas[offset : offset + per_page]]
    response = {
        "genre": genre,
        "region": region,
        "datas": datas,
        "page": page,
        "page_limit": page_limit,
    }
    return render(request, "search.html", response)
