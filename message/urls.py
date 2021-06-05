from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('', views.ViewIndex.as_view(), name='index'),
    path('post/<int:pk>', views.ViewPost.as_view(), name='view_post'),
    path('community/<slug:slug>', views.ViewCommunity.as_view(), name='view_community'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)