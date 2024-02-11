from django.shortcuts import render
from django.conf import settings
from django.db import connection
from django.http import HttpResponse
import pandas as pd
import numpy as np
import csv
from sqlalchemy import create_engine
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from .models import (
    FoodModel,
    DrinkModel,
    BarModel,
    SightModel,
    HotelModel,
    RestaurantModel,
)

# Create your views here.
static_root = settings.STATIC_URL
db_dir = "sqlite:///db.sqlite3"


def init_view(request):
    return render(request, "init/index.html")


def init_food(request):
    path = os.path.join(settings.BASE_DIR, "static", "food.csv")

    conn = create_engine(db_dir)

    csv_file = pd.read_csv(path)
    csv_file["id"] = np.arange(csv_file.shape[0])
    result = csv_file.to_sql("food", con=conn, if_exists="replace", index=False)
    # with open(path, "r", newline="", encoding="utf-8") as file:
    #     csv_reader = csv.DictReader(file)

    #     for i, row in enumerate(csv_reader):
    #         data_to_save = FoodModel(
    #             id=i,
    #             title=row["title"],
    #             address=row["address"],
    #             phone=row["phone"],
    #             score=row["score"],
    #             open_time=row["open_time"],
    #             comment1=row["comment1"],
    #             comment2=row["comment2"],
    #             comment3=row["comment3"],
    #         )
    #         data_to_save.save()
    #         # print(row)

    content = {
        "path": path,
        # "file": csv_file,
        # "length": len(csv_file),
    }
    return render(request, "init/result.html", context=content)


def init_drink(request):
    path = os.path.join(settings.BASE_DIR, "static", "drink.csv")

    conn = create_engine(db_dir)

    csv_file = pd.read_csv(path)
    csv_file["id"] = np.arange(csv_file.shape[0])
    result = csv_file.to_sql("drink", con=conn, if_exists="replace", index=False)

    content = {
        "path": path,
        "file": csv_file,
        "length": len(csv_file),
        "result": result,
    }
    return render(request, "init/result.html", context=content)


def init_bar(request):
    path = os.path.join(settings.BASE_DIR, "static", "bar.csv")

    conn = create_engine(db_dir)

    csv_file = pd.read_csv(path)
    csv_file["id"] = np.arange(csv_file.shape[0])
    result = csv_file.to_sql("bar", con=conn, if_exists="replace", index=False)

    content = {
        "path": path,
        "file": csv_file,
        "length": len(csv_file),
        "result": result,
    }
    return render(request, "init/result.html", context=content)


def init_sight(request):
    path = os.path.join(settings.BASE_DIR, "static", "sight.csv")

    conn = create_engine(db_dir)

    csv_file = pd.read_csv(path)
    csv_file["id"] = np.arange(csv_file.shape[0])
    result = csv_file.to_sql("sight", con=conn, if_exists="replace", index=False)

    content = {
        "path": path,
        "file": csv_file,
        "length": len(csv_file),
        "result": result,
    }
    return render(request, "init/result.html", context=content)


def init_hotel(request):
    path = os.path.join(settings.BASE_DIR, "static", "hotel.csv")

    conn = create_engine(db_dir)

    csv_file = pd.read_csv(path)
    csv_file["id"] = np.arange(csv_file.shape[0])
    result = csv_file.to_sql("hotel", con=conn, if_exists="replace", index=False)

    content = {
        "path": path,
        "file": csv_file,
        "length": len(csv_file),
        "result": result,
    }
    return render(request, "init/result.html", context=content)


def init_restaurant(request):
    path = os.path.join(settings.BASE_DIR, "static", "restaurant.csv")

    conn = create_engine(db_dir)

    csv_file = pd.read_csv(path)
    csv_file["id"] = np.arange(csv_file.shape[0])
    result = csv_file.to_sql("restaurant", con=conn, if_exists="replace", index=False)

    content = {
        "path": path,
        "file": csv_file,
        "length": len(csv_file),
        "result": result,
    }
    return render(request, "init/result.html", context=content)


uri = os.environ.get("MONGO_URL")
client = MongoClient(uri, server_api=ServerApi("1"))


def init_food_mongo(request):
    try:
        client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
        db = client["AnthonyHsu"]
        collection = db["food"]
        path = os.path.join(settings.BASE_DIR, "static", "restaurant.csv")
        csv_file = pd.read_csv(path)
        csv_file["id"] = np.arange(csv_file.shape[0])
        result = collection.insert_many(csv_file.to_dict("records"))

        content = {
            "path": path,
            "file": csv_file,
            "length": len(csv_file),
            "result": result,
        }
        return render(request, "init/result.html", content)
    except Exception as e:
        return HttpResponse(e)
    pass
