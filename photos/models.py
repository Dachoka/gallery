from django.db import models
import datetime as dt

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length = 100)
    description = models.TextField()
    

class Location(models.Model):
    location = models.CharField(max_length = 60)

    def __str__(self):
        return self.location


class Category(models.Model):
    category = models.CharField(max_length= 30)

    def __str__(self):
        return self.category



