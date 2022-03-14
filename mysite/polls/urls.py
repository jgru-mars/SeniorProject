from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('floor/', views.floor, name='floor'),
    path('floor/image/', views.image, name='image'),
]