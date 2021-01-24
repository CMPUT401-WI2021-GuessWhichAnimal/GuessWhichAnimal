from django.urls import path

from . import views

urlpatterns = [
    path('', views.field, name='field'),
    path('increase/', views.increase_score, name='increase'),
]