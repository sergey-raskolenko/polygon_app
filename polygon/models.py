from django.contrib.gis.db import models


class PolygonModel(models.Model):
    """Модель для представления полигона"""

    name = models.CharField(max_length=100, verbose_name='Название')
    polygon = models.PolygonField(
        verbose_name='Координаты полигона', null=True, blank=True
    )
    intersects_antimeridian = models.BooleanField(
        verbose_name='Признак пересечения антимеридиана', null=True, blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Polygon'
        verbose_name_plural = 'Polygons'
        db_table = 'polygon'
        ordering = ['name']
