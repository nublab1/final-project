
from django.contrib import admin
from django.urls import path 
from .views import *


urlpatterns = [

        path('', index, name='index'),
        path('about/', about, name='about'),
        path('services/', services, name='services'),
        path('contact/', contact, name='contact'),
        path('packages/', packages, name='packages'),
        path('team/', team, name='team'),
        path('testimonials/', testimonials, name='testimonials'),
        path('404/', error_404_view, name='error_404'),


]