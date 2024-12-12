from django.urls import path

from car.views import index, CarListView, CarDetailView, CarUpdateView, CarDeleteView, CarCreateView, \
    CarCheckupDetailView

urlpatterns = [
    path("", index, name="index"),
    path("car/", CarListView.as_view(), name="car_list"),
    path("car/<int:pk>", CarDetailView.as_view(), name="car-detail"),
    path("car/<int:pk>/update/", CarUpdateView.as_view(), name="car-update"),
    path("car/<int:pk>/delete/", CarDeleteView.as_view(), name="car-delete"),
    path("car/create/", CarCreateView.as_view(), name="car-create"),
    path("car/<int:pk>/checkup", CarCheckupDetailView.as_view(), name="car-checkup")

]

app_name = "car"
