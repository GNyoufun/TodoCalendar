from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("todoAdd", views.todoAddOn, name="todoAddOn")
]
