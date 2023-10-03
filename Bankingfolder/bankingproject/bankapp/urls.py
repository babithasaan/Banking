from . import views
from django.urls import path

urlpatterns = [
        path('',views.index, name='index'),
        path('login/', views.login, name="login"),
        path('register/', views.registerin, name="register"),
        path('newform/', views.newform, name="newform"),
        path('logout', views.logout, name="logout")
    ]

