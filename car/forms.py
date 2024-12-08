from django import forms


class CarSearchWinForm(forms.Form):
    win_code = forms.IntegerField(
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Search by WIN"
        })
    )
