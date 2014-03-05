from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import MapView

# Create your tests here.

class MapViewTestCase(TestCase):

    def test_map_view_ranges(self):

        MV = MapView()
        MV.name = 'Test Map View'

        with self.assertRaises(ValidationError):
            MV.latitude = -91.0
            MV.longitude = 0.0
            MV.zoom = 14
            MV.save()

        with self.assertRaises(ValidationError):
            MV.latitude = 91.0
            MV.longitude = 0.0
            MV.zoom = 14
            MV.save()

        with self.assertRaises(ValidationError):
            MV.latitude = 0.0
            MV.longitude = -91.0
            MV.zoom = 14
            MV.save()

        with self.assertRaises(ValidationError):
            MV.latitude = 0.0
            MV.longitude = 91.0
            MV.zoom = 14
            MV.save()

        with self.assertRaises(ValidationError):
            MV.latitude = 0.0
            MV.longitude = 0.0
            MV.zoom = -1
            MV.save()

        with self.assertRaises(ValidationError):
            MV.latitude = 0.0
            MV.longitude = 0.0
            MV.zoom = 20
            MV.save()

        # verify that something can be saved

        MV.latitude = -76.616
        MV.longitude = 39.329
        MV.zoom = 14
        MV.save()
        self.assertEqual(len(MapView.objects.all()),1)
        MV.delete()
