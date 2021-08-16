from django.conf.urls import url

from backend import views

urlpatterns = [
    url("^$", views.index),
    url("json", views.json_view, name="json")
]
