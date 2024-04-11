from django.urls import path

from polygon.apps import PolygonConfig
from polygon.views import PolygonCreateView, PolygonListView

app_name = PolygonConfig.name


urlpatterns = [
    path('create/', PolygonCreateView.as_view(), name='polygon_create'),
    path('list/', PolygonListView.as_view(), name='polygon_list'),
]
