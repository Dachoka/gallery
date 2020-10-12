from django.db import models
import datetime as dt

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length = 100)
    description = models.TextField()
    location = models.ForeignKey('Location',on_delete=models.CASCADE)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    date_taken = models.DateTimeField(auto_now_add=True, null=True)
    

class Location(models.Model):
    location = models.CharField(max_length = 60)

    def save_location(self):
        self.save()

    def update_location(self):
        self.update()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.location


class Category(models.Model):
    category = models.CharField(max_length= 30)

    def save_category(self):
        self.save()

    def update_category(self):
        self.update()

    

    def __str__(self):
        return self.category



