from django.test import TestCase
from .models import Image, Location, Category

# Create your tests here.

class LocationTestCase(TestCase):

    def setUp(self):
        self.nairobi = Location(location = 'Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi, Location))

    def test_save_method(self):
        self.nairobi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_update_method(self):
        self.nairobi.save_location()
        self.nairobi = Location.objects.filter(location = 'Nairobi').update(location = 'Kisumu')
        self.location_update = Location.objects.get(location = 'Kisumu')
        self.assertEqual(self.location_update.location, 'Kisumu')

