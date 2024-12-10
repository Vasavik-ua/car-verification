from django.urls import path

from car.views import index, CarListView, CarDetailView, CarUpdateView

urlpatterns = [
    path("", index, name="index"),
    path("car/", CarListView.as_view(), name="car_list"),
    path("car/<int:pk>", CarDetailView.as_view(), name="car-detail"),
    path("car/<int:pk>/update/", CarUpdateView.as_view(), name="car-update")

]

app_name = "car"
