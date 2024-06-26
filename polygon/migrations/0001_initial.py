# Generated by Django 4.2.11 on 2024-04-13 09:47

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PolygonModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "polygon",
                    django.contrib.gis.db.models.fields.PolygonField(
                        blank=True, null=True, srid=4326
                    ),
                ),
                ("intersects_antimeridian", models.BooleanField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Polygon",
                "verbose_name_plural": "Polygons",
                "db_table": "polygon",
                "ordering": ["name"],
            },
        ),
    ]
