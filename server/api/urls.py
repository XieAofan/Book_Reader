from django.urls import path

from . import views
urlpatterns = [
    path('getBookshelf', views.getBookshelf, name='getBookshelf'),
    path('getChapterList', views.getChapterList, name='getChapterList'),
    path('getBookContent', views.getBookContent, name='getBookContent'),

]