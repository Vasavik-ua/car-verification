from django import forms
from django.contrib.auth.forms import UserCreationForm

from car.models import CompanyCheckUp


class CarSearchWinForm(forms.Form):
    win_code = forms.CharField(
        max_length=255,
        required=True,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Search by WIN"
        })
    )


# class CarSearchCheckUp(forms.Form):
#     performed_by = forms.CharField(
#         max_length=255,
#         required=True,
#         label="",
#         widget=forms.TextInput(attrs={
#             "placeholder": "Search by Performed By"
#         })
#     )


class CompanyCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CompanyCheckUp
        fields = UserCreationForm.Meta.fields + (
            "country",
            "city",
        )
