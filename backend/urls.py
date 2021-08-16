from django.conf.urls import url

from backend import views

urlpatterns = [
    url("^$", views.index),
    url("search", views.search),
    url("json", views.json_view, name="json"),
]
