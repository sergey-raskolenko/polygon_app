from django import forms
from .models import PolygonModel


class PolygonForm(forms.ModelForm):
    class Meta:
        model = PolygonModel
        fields = ['name', 'polygon']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in range(4):
            self.fields[f'latitude_{i+1}'] = forms.FloatField(label=f'Latitude {i+1}')
            self.fields[f'longitude_{i+1}'] = forms.FloatField(label=f'Longitude {i+1}')
