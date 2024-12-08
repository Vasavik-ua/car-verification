from django.urls import path

from car.views import index, CarListView

urlpatterns = [
    path("", index, name="index"),
    path("car/", CarListView.as_view(), name="car_list"),

]

app_name = "car"
