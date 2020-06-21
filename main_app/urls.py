from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.index, name = "inicio"),
    path('', views.index, name = "index"),
]
