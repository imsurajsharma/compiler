from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('test/',views.test, name='test'),
    path('embed/',views.embed, name='embed'),
]
