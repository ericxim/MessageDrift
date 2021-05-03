from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('create/', views.create_post, name='create_post'),
    path('post/<str:pk>/', views.view_post, name='view_post'),

]