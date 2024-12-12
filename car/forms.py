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


class CarSearchCheckUp(forms.Form):
    performed_by = forms.CharField(
        max_length=255,
        required=True,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Search by Performed By"
        })
    )
