from django.urls import path

from . import views

urlpatterns = [
    path('trading/', views.index, name='index'),
    path('', views.start, name='start'),
]