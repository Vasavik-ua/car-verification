from django.urls import path

from car.views import (
    index,
    CarListView,
    CarDetailView,
    CarUpdateView,
    CarDeleteView,
    CarCreateView,
    CarCheckupDetailView,
    CheckUpCreateView,
    CheckUpUpdateView,
    CheckUpDeleteView,
    CarOwnerDetailView,
    CarOwnerCreateView,
    CarOwnerUpdateView,
    CarOwnerDeleteView,
    CompanyCheckUpDetailView,
    CompanyCheckUpCreateView,
    CompanyCheckUpUpdateView,
    logout,
)

urlpatterns = [
    path("", index, name="index"),
    path("car/", CarListView.as_view(), name="car_list"),
    path("logout/", logout, name="logout"),
    path("car/<int:pk>", CarDetailView.as_view(), name="car-detail"),
    path("car/<int:pk>/update/", CarUpdateView.as_view(), name="car-update"),
    path("car/<int:pk>/delete/", CarDeleteView.as_view(), name="car-delete"),
    path("car/create/", CarCreateView.as_view(), name="car-create"),
    path(
        "car/<int:pk>/checkup/",
        CarCheckupDetailView.as_view(),
        name="car-checkup"
    ),
    path(
        "car/checkup/create/",
        CheckUpCreateView.as_view(),
        name="checkup-create"),
    path(
        "car/checkup/<int:pk>/update/",
        CheckUpUpdateView.as_view(),
        name="checkup-update",
    ),
    path(
        "car/checkup/<int:pk>/delete/",
        CheckUpDeleteView.as_view(),
        name="checkup-delete",
    ),
    path(
        "car/<int:pk>/owner",
        CarOwnerDetailView.as_view(),
        name="car-owner-detail"),
    path(
        "car/owner/create/",
        CarOwnerCreateView.as_view(),
        name="owner-create"),
    path(
        "car/owner/<int:pk>/update/",
        CarOwnerUpdateView.as_view(),
        name="owner-update"
    ),
    path(
        "car/owner/<int:pk>/delete/",
        CarOwnerDeleteView.as_view(),
        name="owner-delete"
    ),
    path(
        "car/checkup/company/<int:pk>",
        CompanyCheckUpDetailView.as_view(),
        name="company-detail",
    ),
    path(
        "car/checkup/company/create/",
        CompanyCheckUpCreateView.as_view(),
        name="company-create",
    ),
    path(
        "car/checkup/company/update/<int:pk>/",
        CompanyCheckUpUpdateView.as_view(),
        name="company-update",
    ),
]

app_name = "car"
