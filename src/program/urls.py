from django.urls import path
from . import views

urlpatterns = [
    path("status", views.status, name="status"),
    path("", views.main, name="main"),
    path("sayHello/", views.say_hello, name="say-hello"),
]
