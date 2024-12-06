from django.urls import path

from car.views import index

urlpatterns = [
    path("", index, name="index")
]

app_name = "car"
