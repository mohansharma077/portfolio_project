# URL patterns for the portfolio app
from django.urls import path
from . import home

urlpatterns = [
    path('', home.index, name='index'),
    path('projects/', home.projects, name='projects'),
    path('contact/', home.contact, name='contact'),
]