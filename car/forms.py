from django import forms


class CarSearchWinForm(forms.Form):
    win_code = forms.CharField(
        max_length=255,
        required=True,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Search by WIN"
        })
    )
