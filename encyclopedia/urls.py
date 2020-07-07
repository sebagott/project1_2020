from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index_redirect, name="index_redirect"),
    path("wiki/", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("wiki/<str:title>/edit", views.edit, name="edit"),
    path("wiki/search/", views.search, name="search"),
    path("wiki/random/", views.random, name="random"),
    path("wiki/create/", views.create, name="create"),
]
