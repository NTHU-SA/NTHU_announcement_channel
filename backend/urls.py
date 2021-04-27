from django.conf.urls import url

from backend import views

urlpatterns = [url("^$", views.index)]
