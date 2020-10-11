from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    '''
    view function that renders the homepage
    '''
    return HttpResponse('Welcome to Photo Blast')