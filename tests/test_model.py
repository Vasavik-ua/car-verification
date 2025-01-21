from django.test import TestCase

from car.models import Car, CarOwner, CompanyCheckUp, CheckUpCar


class TestModel(TestCase):
    def test_verbose_name_car(self):
        verbose_name = Car._meta.verbose_name
        self.assertEqual(verbose_name, "car")

    def test_verbose_name_plural_car(self):
        verbose_name_plural = Car._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, "cars")

    def test_verbose_name_carowner(self):
        verbose_name = CarOwner._meta.verbose_name
        self.assertEqual(verbose_name, "car owner")

    def test_verbose_name_plural_carowner(self):
        verbose_name_plural = CarOwner._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, "car owners")

    def test_verbose_name_companycheckup(self):
        verbose_name = CompanyCheckUp._meta.verbose_name
        self.assertEqual(verbose_name, "user")

    def test_verbose_name_plural_companycheckup(self):
        verbose_name_plural = CompanyCheckUp._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, "users")

    def test_verbose_name_checkupcar(self):
        verbose_name = CheckUpCar._meta.verbose_name
        self.assertEqual(verbose_name, "check up car")

    def test_verbose_name_plural_checkupcar(self):
        verbose_name_plural = CheckUpCar._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, "check up cars")