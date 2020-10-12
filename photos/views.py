from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from .models import Image, Category,Location

# Create your views here.
def homepage(request):
    '''
    view function that renders the homepage
    '''
    return render(request,'homepage.html')

def search_category(request):
    if 'category' in request.GET and request.GET["category"]:
        search_category = request.GET.get("category")
        searched_categories = Image.search_by_category(search_category)
        message = f"{search_category}"

        return render(request, 'categorysearch.html', {"message":message, "images":searched_categories})

    else:
        message = "You have not searched for any category"
        return render(request, 'categorysearch.html',{"message":message})

        


