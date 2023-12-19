from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<int:year>/", views.home, name="home"),
    path("<int:year>/<int:month>/", views.home, name="home"),
    path("todoAdd", views.todoAddOn, name="todoAddOn")
]
