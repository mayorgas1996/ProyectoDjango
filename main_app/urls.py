from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.index, name = "inicio"),
    path('', views.index, name = "index"),
    path('registro/', views.register_page, name = "register"),
    path('login/', views.login_page, name = "login"),
    path('logout/', views.logout_user, name = "logout"),
]
