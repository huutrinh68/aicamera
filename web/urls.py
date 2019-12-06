from django.conf.urls import url
from web import views
from django.urls import path

urlpatterns = [
    url(r'^video_feed/$', views.video_feed, name='video_feed'),
    url(r'^chat/$', views.index, name='chat'),
    url(r'^camera/$', views.camera, name='camera'),
    path('<str:room_name>/', views.room, name='room'),
]