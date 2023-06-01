from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home),
    path("books", views.books),
    path("about", views.about),
    path("contact", views.contact),
]