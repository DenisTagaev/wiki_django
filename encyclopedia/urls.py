from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.entry, name="e_entry"),
    path("new_entry", views.new_entry, name="new_entry"),
    path("error", views.non_existent_entry, name="error"),
]
