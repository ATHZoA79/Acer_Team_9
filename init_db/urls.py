from django.urls import path
from . import views
from django.contrib.admin.views.decorators import staff_member_required


urlpatterns = [
    path("", views.init_view),
    path("food/", views.init_food),
    path("drink/", views.init_drink),
    path("bar/", views.init_bar),
    path("sight/", views.init_sight),
    path("hotel/", views.init_hotel),
    path("restaurant/", views.init_restaurant),
]
# urlpatterns = [
#     path("food/", staff_member_required(views.init_food)),
#     path("drink/", staff_member_required(views.init_drink)),
#     path("bar/", staff_member_required(views.init_bar)),
#     path("sight/", staff_member_required(views.init_sight)),
#     path("hotel/", staff_member_required(views.init_hotel)),
#     path("restaurant/", staff_member_required(views.init_restaurant)),
# ]
