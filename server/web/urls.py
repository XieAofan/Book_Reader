from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reader',views.reader, name='raeder'),
    path('test',views.test, name='test'),
    path('login',views.my_login, name='login'),
    path('logout',views.my_logout, name='logout'),
]