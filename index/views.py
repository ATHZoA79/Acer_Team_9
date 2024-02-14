from django.http import HttpResponse, HttpRequest
from django.forms.models import model_to_dict
from django.shortcuts import render, redirect
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
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
    page = int(page)
    per_page = request.GET.get("per_page", 10)
    per_page = int(per_page)
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


uri = os.environ.get("MONGO_URL")
client = MongoClient(str(uri), server_api=ServerApi("1"))
db = client["AnthonyHsu"]


def search_mongo(request: HttpRequest):
    page = request.GET.get("page", 1)
    page = int(page)
    per_page = request.GET.get("per_page", 10)
    per_page = int(per_page)
    region = request.GET.get("region", "")
    genre = request.GET.get("genre", "food")
    offset = (page - 1) * per_page
    GROUP_LIMIT = 5
    if genre == "food":
        collection = db["food"]
        try:
            datas = collection.find({"region": region}).skip(offset).limit(per_page)
            page_limit = collection.count_documents({"region": region})
            datas = list(datas)
            page_limit = page_limit // per_page + 1
            # return HttpResponse(list(datas))
            response = {
                "genre": genre,
                "region": region,
                "datas": datas,
                "page": page,
                "page_limit": page_limit,
            }
            return render(request, "search.html", response)
        except Exception as e:
            contents = [e, region, genre]
            return HttpResponse(contents)
    if genre == "sight":
        collection = db["sight"]
        try:
            datas = collection.find({"region": region}).skip(offset).limit(per_page)
            page_limit = collection.count_documents({"region": region})
            datas = list(datas)
            page_limit = page_limit // per_page + 1
            # return HttpResponse(list(datas))
            response = {
                "genre": genre,
                "region": region,
                "datas": datas,
                "page": page,
                "page_limit": page_limit,
            }
            return render(request, "search.html", response)
        except Exception as e:
            contents = [e, region, genre]
            return HttpResponse(contents)
    if genre == "hotel":
        collection = db["hotel"]
        try:
            datas = collection.find({"region": region}).skip(offset).limit(per_page)
            page_limit = collection.count_documents({"region": region})
            datas = list(datas)
            page_limit = page_limit // per_page + 1
            # return HttpResponse(list(datas))
            response = {
                "genre": genre,
                "region": region,
                "datas": datas,
                "page": page,
                "page_limit": page_limit,
            }
            return render(request, "search.html", response)
        except Exception as e:
            contents = [e, region, genre]
            return HttpResponse(contents)
    if genre == "bar":
        collection = db["bar"]
        try:
            datas = collection.find({"region": region}).skip(offset).limit(per_page)
            page_limit = collection.count_documents({"region": region})
            datas = list(datas)
            page_limit = page_limit // per_page + 1
            # return HttpResponse(list(datas))
            response = {
                "genre": genre,
                "region": region,
                "datas": datas,
                "page": page,
                "page_limit": page_limit,
            }
            return render(request, "search.html", response)
        except Exception as e:
            contents = [e, region, genre]
            return HttpResponse(contents)
    if genre == "restaurant":
        collection = db["restaurant"]
        try:
            datas = collection.find({"region": region}).skip(offset).limit(per_page)
            page_limit = collection.count_documents({"region": region})
            datas = list(datas)
            page_limit = page_limit // per_page + 1
            # return HttpResponse(list(datas))
            response = {
                "genre": genre,
                "region": region,
                "datas": datas,
                "page": page,
                "page_limit": page_limit,
            }
            return render(request, "search.html", response)
        except Exception as e:
            contents = [e, region, genre]
            return HttpResponse(contents)
