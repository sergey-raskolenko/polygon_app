from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from polygon.forms import PolygonForm
from polygon.models import PolygonModel
from django.contrib.gis.geos import Polygon


class PolygonCreateView(CreateView):
    """
    Контроллер для создания экземпляра PolygonModel
    """

    model = PolygonModel
    form_class = PolygonForm
    success_url = reverse_lazy('polygon:polygon_list')

    def form_invalid(self, form):
        messages.error(self.request, 'Неверные данные')
        return super().form_invalid(form)

    def form_valid(self, form):
        polygon = form.save(commit=False)
        intersects_antimeridian = False
        for i in range(4):
            if form.cleaned_data[f'longitude_{i + 1}'] > 180:
                form.cleaned_data[f'longitude_{i + 1}'] -= 360
                intersects_antimeridian = True
        polygon.intersects_antimeridian = intersects_antimeridian
        points = [
            [
                (
                    form.cleaned_data[f'latitude_{i + 1}'],
                    form.cleaned_data[f'longitude_{i + 1}'],
                )
                for i in range(4)
            ]
        ]
        if points[0] != points[-1]:
            points.append(points[0])
        polygon.polygon = Polygon(points)
        polygon.save()
        return super().form_valid(form)


class PolygonListView(ListView):
    """
    Контроллер для отображения списка экземпляров PolygonModel
    """

    model = PolygonModel
    context_object_name = 'polygons'
