import django_filters
from .models import Image

class ImageFilter(django_filters.FilterSet):
    class Meta:
        model = Image
        fields = {'location__location': ['icontains']}
