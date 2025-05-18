from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_sample),
    path('description/', views.get_sample_description),
    path('image/', views.get_sample_image),
    path('audio/', views.get_sample_audio),
]