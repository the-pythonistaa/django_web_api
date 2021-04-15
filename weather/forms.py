from django import forms


class WeatherForm(forms.Form):
    city = forms.CharField(
        label="Enter City:"
    )