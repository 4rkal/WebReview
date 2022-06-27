from django.urls import path

from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
    path("addsite/", views.addsite, name="addsite"),
    path("docs/", views.docs, name="docs"),
    path("home/", views.home, name="home"),
    path("all/", views.viewall, name="viewall"),

]