from rest_framework import serializers

from polygon.models import PolygonModel


class PolygonModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = PolygonModel
        fields = '__all__'


class PolygonModelCreateSerializer(serializers.ModelSerializer):
    polygon = serializers.ListField(
        child=serializers.ListField(
            child=serializers.FloatField(), min_length=2, max_length=2
        ),
        min_length=4,
        max_length=4,
    )

    class Meta:
        model = PolygonModel
        fields = (
            'name',
            'polygon',
        )

    def validate(self, data):
        intersects_antimeridian = False
        processed_polygon = []

        for point in data['polygon']:
            if point[1] > 180:
                point[1] -= 360
                intersects_antimeridian = True
            processed_polygon.append(point)

        if processed_polygon[0] != processed_polygon[-1]:
            processed_polygon.append(processed_polygon[0])

        data['intersects_antimeridian'] = intersects_antimeridian
        data['polygon'] = processed_polygon
        return data
