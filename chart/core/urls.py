
from django.urls import path
from .views import *
urlpatterns = [
    path('', home),
    path('example/', example),
    path('line/', slice),
    path('bar/', bars),
    path('radar/', radar),
    path('pie/', pie),
    path('polar/', polar),
    path('bublle/', bublle),
    path('area/', area),
]