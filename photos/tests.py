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
        self.location_update = Location.objects.get(id = 1)
        self.assertEqual(self.location_update.location, 'Kisumu')

    def test_delete_method(self):
        self.nairobi.save_location()
        self.nairobi = Location.objects.get(id = 1)
        self.nairobi.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)==0)


class CategoryTestCase(TestCase):

    def setUp(self):
        self.fashion = Category(category = 'Fashion')

    def test_instance(self):
        self.assertTrue(isinstance(self.fashion, Category))

    def test_save_method(self):
        self.fashion.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)

    def test_update_method(self):
        self.fashion.save_category()
        self.fashion = Category.objects.filter(category = 'Fashion').update(category = 'Pets')
        self.category_update = Category.objects.get(id = 1)
        self.assertEqual(self.category_update.category,'Pets')

    def test_delete_method(self):
        self.fashion.save_category()
        self.fashion = Category.objects.get(id = 1)
        self.fashion.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)


class ImageTestCase(TestCase):

    def setUp(self):
        self.wildlife = Category(category = 'Wildlife')
        self.wildlife.save_category()
        self.mandera = Location(location = 'Mandera')
        self.mandera.save_location()

        self.image = Image( image = 'images/hyena.jpeg', name = 'Hyena', description = 'Fascinating Hyenas', location = self.mandera, category = self.wildlife)

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))



