from django.urls import path
from .views import train

urlpatterns = [
    path('', train, name='train')
]