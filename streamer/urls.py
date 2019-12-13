from streamer import views
from django.urls import path

urlpatterns = [
    path('video_feed/', views.video_feed, name='video_feed'),
    path('camera/', views.camera, name='camera'),
]