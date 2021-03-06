from django.db import models
from pyuploadcare.dj.models import ImageField
import datetime as dt

# Create your models here.
class Image(models.Model):
    image = ImageField(blank = True, manual_crop = "")
    name = models.CharField(max_length = 100)
    description = models.TextField()
    location = models.ForeignKey('Location',on_delete=models.CASCADE)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    date_taken = models.DateTimeField(auto_now_add=True, null=True)


    def save_image(self):
        self.save()

    def update_image(self, new_image):
        self.update(image= new_image)

    def delete_image(self):
        self.delete()

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def filter_by_location(cls,location):
        located_images = cls.objects.filter(location = location)
        return located_images

    @classmethod
    def search_by_category(cls, search_category):
        found_items = cls.objects.filter(category__category__icontains=search_category)
        return found_items

    

class Location(models.Model):
    location = models.CharField(max_length = 60)

    def save_location(self):
        self.save()

    def update_location(self, new_location):
        self.update(location = new_location)

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.location


class Category(models.Model):
    category = models.CharField(max_length= 30)

    def save_category(self):
        self.save()

    def update_category(self, new_category):
        self.update(category = new_category)

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.category



