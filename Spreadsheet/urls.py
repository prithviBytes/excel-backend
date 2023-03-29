# authentication_app/urls.py

from django.urls import path
from . import views


urlpatterns = [
    path('create', views.create, name='create-spreadsheet'),
    path('update', views.update, name='update-spreadsheet'),
]
