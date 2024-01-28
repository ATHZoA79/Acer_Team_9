from django.db import models


# Create your models here.
class FoodModel(models.Model):
    region = models.TextField("region")
    title = models.TextField("title")
    address = models.TextField("address")
    phone = models.TextField("phone")
    score = models.TextField("score")
    open_time = models.TextField("open_time")
    comment1 = models.TextField("comment1")
    comment2 = models.TextField("comment2")
    comment3 = models.TextField("comment3")

    class Meta:
        db_table = "food"
        indexes = [
            models.Index(fields=["region"]),
        ]


class DrinkModel(models.Model):
    region = models.TextField("region")
    title = models.TextField("title")
    address = models.TextField("address")
    phone = models.TextField("phone")
    score = models.TextField("score")
    open_time = models.TextField("open_time")
    comment1 = models.TextField("comment1")
    comment2 = models.TextField("comment2")
    comment3 = models.TextField("comment3")

    class Meta:
        db_table = "drink"
        indexes = [
            models.Index(fields=["region"]),
        ]


class BarModel(models.Model):
    region = models.TextField("region")
    title = models.TextField("title")
    address = models.TextField("address")
    phone = models.TextField("phone")
    score = models.TextField("score")
    open_time = models.TextField("open_time")
    comment1 = models.TextField("comment1")
    comment2 = models.TextField("comment2")
    comment3 = models.TextField("comment3")

    class Meta:
        db_table = "bar"
        indexes = [
            models.Index(fields=["region"]),
        ]


class SightModel(models.Model):
    region = models.TextField("region")
    title = models.TextField("title")
    address = models.TextField("address")
    phone = models.TextField("phone")
    score = models.TextField("score")
    open_time = models.TextField("open_time")
    comment1 = models.TextField("comment1")
    comment2 = models.TextField("comment2")
    comment3 = models.TextField("comment3")

    class Meta:
        db_table = "sight"
        indexes = [
            models.Index(fields=["region"]),
        ]


class HotelModel(models.Model):
    region = models.TextField("region")
    title = models.TextField("title")
    address = models.TextField("address")
    phone = models.TextField("phone")
    score = models.TextField("score")
    open_time = models.TextField("open_time")
    comment1 = models.TextField("comment1")
    comment2 = models.TextField("comment2")
    comment3 = models.TextField("comment3")

    class Meta:
        db_table = "hotel"
        indexes = [
            models.Index(fields=["region"]),
        ]


class RestaurantModel(models.Model):
    region = models.TextField("region")
    title = models.TextField("title")
    address = models.TextField("address")
    phone = models.TextField("phone")
    score = models.TextField("score")
    open_time = models.TextField("open_time")
    comment1 = models.TextField("comment1")
    comment2 = models.TextField("comment2")
    comment3 = models.TextField("comment3")

    class Meta:
        db_table = "restaurant"
        indexes = [
            models.Index(fields=["region"]),
        ]
