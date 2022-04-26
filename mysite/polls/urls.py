from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('floor/', views.floor, name='floor'),
    path('room/', views.room, name='room'),
    path('image/', views.image, name='image'),
    path('editor/', views.editor, name='editor'),
    path('editor/image/', views.editorimage, name='editorimage'),
    path('editor/runfunction/', views.addToFile, name='editorfunction'),
    path('favicon.ico', RedirectView.as_view(url='static/favicon.ico'))
]
