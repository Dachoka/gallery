from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django_filters.views import FilterView 
from . import views




urlpatterns = [
    path('',views.homepage, name='home'),
    path('search/', views.search_category, name = 'search_category'),
    path('filter/', views.filter_location, name = 'filter_location'),
    path('about/', views.about, name = 'about')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)