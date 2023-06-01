from django.contrib import admin
from django.urls import path
from . import views
from .pages import about



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home),
    path("books", views.books),
    path("about", about.main),
    path("contact", about.contact),
]