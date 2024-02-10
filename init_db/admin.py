from django.contrib import admin
from .models import (
    FoodModel,
    DrinkModel,
    SightModel,
    HotelModel,
    RestaurantModel,
    BarModel,
)


# Register your models here.
@admin.register(FoodModel)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in FoodModel._meta.get_fields()]


@admin.register(DrinkModel)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DrinkModel._meta.get_fields()]


@admin.register(SightModel)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SightModel._meta.get_fields()]


@admin.register(HotelModel)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in HotelModel._meta.get_fields()]


@admin.register(RestaurantModel)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in RestaurantModel._meta.get_fields()]


@admin.register(BarModel)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BarModel._meta.get_fields()]
