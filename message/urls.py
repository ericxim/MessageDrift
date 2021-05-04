from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('create/', views.create_post, name='create_post'),
    path('post/', views.ViewPost.as_view(), name='view_post'),
    path('community/<str:name>', views.ViewCommunity.as_view(), name='view_community'),

]