from django import forms
from polygon.models import Polygon


class PolygonForm(forms.ModelForm):
    class Meta:
        model = Polygon
        fields = ['name',]

    latitude_1 = forms.FloatField(label='Latitude 1')
    longitude_1 = forms.FloatField(label='Longitude 1')
    latitude_2 = forms.FloatField(label='Latitude 2')
    longitude_2 = forms.FloatField(label='Longitude 2')
