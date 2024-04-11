from django.contrib.gis.db import models


class Polygon(models.Model):
    name = models.CharField(max_length=100)
    polygon = models.PolygonField()
    intersects_antimeridian = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Polygon'
        verbose_name_plural = 'Polygons'
        db_table = 'polygon'
        ordering = ['name']
