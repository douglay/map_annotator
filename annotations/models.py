from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.

class MapView(models.Model):
    
    MIN_LAT_LONG = -90.0
    MAX_LAT_LONG = 90.0
    MIN_ZOOM = 0
    MAX_ZOOM = 18

    name = models.CharField(max_length=100)
    latitude = models.FloatField(
        validators=[MinValueValidator(MIN_LAT_LONG),
                    MaxValueValidator(MAX_LAT_LONG)])
    longitude = models.FloatField(
        validators=[MinValueValidator(MIN_LAT_LONG),
                    MaxValueValidator(MAX_LAT_LONG)])
    zoom = models.IntegerField(
        validators=[MinValueValidator(MIN_ZOOM),
                    MaxValueValidator(MAX_ZOOM)])

    def save(self, *args, **kwargs):
        if (self.latitude < MapView.MIN_LAT_LONG or
            self.latitude > MapView.MAX_LAT_LONG or
            self.longitude < MapView.MIN_LAT_LONG or
            self.longitude > MapView.MAX_LAT_LONG or
            self.zoom < MapView.MIN_ZOOM or
            self.zoom > MapView.MAX_ZOOM):
            raise ValidationError('Value out of range')
        super(MapView, self).save(*args, **kwargs)
