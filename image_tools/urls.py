from django.urls import path

from . import views


app_name = "image_tools"

urlpatterns = [
    path("", views.home, name="home"),
]
