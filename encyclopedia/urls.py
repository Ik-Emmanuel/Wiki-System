from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("all", views.all, name="allpages"),
    path("wiki/<str:title>", views.wiki, name="wiki"),
    path("edit_page/<str:title>", views.edit_page, name="edit_page"),
    path("random_page", views.random_page, name="random_page"),
    path("infosource", views.infosource, name="infosource"),
    path("howto", views.howto, name="howto"),
    path("search", views.search, name="search"),
    path("add_page", views.add_page, name="add_page"),
  



]
