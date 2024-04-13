from django.contrib.gis.geos import Polygon
from rest_framework import status
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    CreateAPIView,
)
from rest_framework.response import Response

from polygon.api.serializers import PolygonModelSerializer, PolygonModelCreateSerializer
from polygon.models import PolygonModel


class PolygonModelListAPIView(ListAPIView):
    """
    Контроллер для вывода списка экземпляров PolygonModel
    """

    queryset = PolygonModel.objects.all()
    serializer_class = PolygonModelSerializer


class PolygonModelCreateAPIView(CreateAPIView):
    """
    Контроллер для создания экземпляра PolygonModel
    """

    serializer_class = PolygonModelCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data.get('name')
        polygon = serializer.validated_data.get('polygon')
        intersects_antimeridian = serializer.validated_data.get(
            'intersects_antimeridian'
        )

        instance = PolygonModel.objects.create(
            name=name, intersects_antimeridian=intersects_antimeridian
        )
        instance.polygon = Polygon(polygon)
        instance.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PolygonModelRUDView(RetrieveUpdateDestroyAPIView):
    """
    Контроллер для просмотра, редактирования и удаления экземпляра PolygonModel
    """

    queryset = PolygonModel.objects.all()
    serializer_class = PolygonModelSerializer
