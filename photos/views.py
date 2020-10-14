from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from .models import Image, Category,Location
from .filters import ImageFilter

# Create your views here.
def homepage(request):
    '''
    view function that renders the homepage
    '''
    all_images = Image.get_all_images()

    return render(request,'homepage.html', {"images":all_images})

def search_category(request):
    if 'category' in request.GET and request.GET["category"]:
        search_category = request.GET.get("category")
        searched_categories = Image.search_by_category(search_category)
        message = f"{search_category}"

        return render(request, 'categorysearch.html', {"message":message, "images":searched_categories})

    else:
        message = "You have not searched for any category"
        return render(request, 'categorysearch.html',{"message":message})

def filter_location(request):
    filter_list = Image.objects.all()
    image_filter = ImageFilter(request.GET, queryset = filter_list)
    return render(request, 'location.html', {"filter":image_filter})

        


