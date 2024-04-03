from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/search", views.index_search, name="wiki_search"),
    path("wiki/<str:entry>", views.entry, name="e_entry"),
    path("new_entry", views.new_entry, name="wiki_new_entry"),
    path("random_entry", views.random_entry, name="random_entry"),
    path("error", views.non_existent_entry, name="wiki_error"),
]
