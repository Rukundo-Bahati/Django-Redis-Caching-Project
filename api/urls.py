"""
URL configuration for api app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.get_data, name='get_data'),
]
