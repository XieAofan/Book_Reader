from django.urls import path

from . import views
urlpatterns = [
    path('getBookshelf', views.getBookshelf, name='getBookshelf'),
]