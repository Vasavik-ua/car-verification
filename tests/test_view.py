from django.test import TestCase
from django.urls import reverse

from car.models import CompanyCheckUp


class LoginTests(TestCase):
    def test_login_required(self):
        url = reverse("car:car_list")
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)

    def test_without_login_home_page(self):
        url = reverse("car:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class ViewTests(TestCase):
    def setUp(self):
        self.user = CompanyCheckUp.objects.create_user(
            username="Vasavik",
            password="Vasavik12345"
        )
        self.client.force_login(self.user)

    def test_view_carlist_page(self):
        response = self.client.get("/car/")
        self.assertEqual(response.status_code, 200)
