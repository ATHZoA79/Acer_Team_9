from django.shortcuts import render
from django.conf import settings
from django.db import connection
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import os
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

    content = {
        "path": path,
        "file": csv_file,
        "length": len(csv_file),
        "result": result,
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
