from django.contrib import admin
from django.urls import path
from .views import home, nomes

urlpatterns = [
    path('home/', home, name='home'),
    path('nomes/', nomes, name='nomes'),
]
