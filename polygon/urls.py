from django.urls import path

from polygon.api.views import (
    PolygonModelRUDView,
    PolygonModelListAPIView,
    PolygonModelCreateAPIView,
)
from polygon.apps import PolygonConfig
from polygon.views import PolygonCreateView, PolygonListView

app_name = PolygonConfig.name


urlpatterns = [
    path('create/', PolygonCreateView.as_view(), name='polygon_create'),
    path('list/', PolygonListView.as_view(), name='polygon_list'),
    path('api/', PolygonModelListAPIView.as_view(), name='api_list'),
    path('api/create/', PolygonModelCreateAPIView.as_view(), name='api_create'),
    path('api/<int:pk>/', PolygonModelRUDView.as_view(), name='api_rud'),
]
