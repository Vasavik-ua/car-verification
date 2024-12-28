from django.contrib.auth.models import AbstractUser
from django.db import models


class Car(models.Model):
    mark = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    win_code = models.CharField(max_length=255, unique=True)
    info_cars = models.OneToOneField(
        "InfoCar", on_delete=models.CASCADE, related_name="cars"
    )


class InfoCar(models.Model):
    country_location = models.CharField(max_length=255)
    city_location = models.CharField(max_length=255)


class CarOwner(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    info_owner = models.ForeignKey(
        InfoCar, on_delete=models.PROTECT, related_name="owners"
    )


class CompanyCheckUp(AbstractUser):
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255, blank=True)


class CheckUpCar(models.Model):
    data_of_execution = models.DateField()
    kilometers = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    body_state = models.CharField(max_length=255, blank=True)
    health_check = models.CharField(max_length=255, blank=True)
    info_checkup = models.ForeignKey(
        InfoCar, on_delete=models.CASCADE, related_name="checkups"
    )
    performed_by = models.ForeignKey(
        CompanyCheckUp, on_delete=models.PROTECT, related_name="company"
    )
