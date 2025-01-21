from django.core.exceptions import ValidationError
from django.test import TestCase

from car.forms import validate_win_code


class FormTest(TestCase):

    def test_validation_win_code(self):
        form = validate_win_code("AYTQ12434TYHGHFH5")
        self.assertEqual(form, "AYTQ12434TYHGHFH5")

    def test_win_code_too_short(self):
        with self.assertRaises(ValidationError) as error:
            validate_win_code("AYTQ12434TYHGH")
        self.assertIn("WIN Code must be 17 digits and Alphanumeric characters", str(error.exception))

    def test_win_code_with_special_symbol(self):
        with self.assertRaises(ValidationError) as error:
            validate_win_code("AYTQ12434TYHGH!!!")
        self.assertIn("WIN Code must be 17 digits and Alphanumeric characters", str(error.exception))
