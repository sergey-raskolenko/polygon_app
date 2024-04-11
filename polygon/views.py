
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from polygon.forms import PolygonForm
from polygon.models import Polygon


class PolygonCreateView(CreateView):
    model = Polygon
    form_class = PolygonForm
    success_url = reverse_lazy('polygon_list')

    def form_valid(self, form):
        polygon = form.save(commit=False)
        latitude_1 = form.cleaned_data['latitude_1']
        longitude_1 = form.cleaned_data['longitude_1']
        latitude_2 = form.cleaned_data['latitude_2']
        longitude_2 = form.cleaned_data['longitude_2']

        if longitude_1 > 180:
            form.cleaned_data['longitude_1'] = longitude_1 - 360
            form.cleaned_data['intersects_antimeridian'] = True
        if longitude_2 > 180:
            form.cleaned_data['longitude_2'] = longitude_2 - 360
            form.cleaned_data['intersects_antimeridian'] = True

        polygon.save()

        return super().form_valid(form)


class PolygonListView(ListView):
    model = Polygon
    context_object_name = 'polygons'
