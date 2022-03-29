from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('floor/', views.floor, name='floor'),
    path('room/', views.room, name='room'),
    path('image/', views.image, name='image'),
]