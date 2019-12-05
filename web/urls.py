from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.video_feed, name='video_feed')
]