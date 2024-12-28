from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from car.models import CompanyCheckUp, Car


class CarSearchWinForm(forms.Form):
    win_code = forms.CharField(
        max_length=255,
        required=True,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by WIN"}
        ),
    )


class CompanyCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CompanyCheckUp
        fields = UserCreationForm.Meta.fields + (
            "country",
            "city",
        )


def validate_win_code(win_code):
    if len(win_code) != 17 or not win_code.isalnum():
        raise ValidationError(
            "WIN Code must be 17 digits and Alphanumeric characters"
        )
    return win_code


class CarCreationForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"

    def clean_win_code(self):
        return validate_win_code(self.cleaned_data["win_code"])
