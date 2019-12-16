from face_detect_app import views
from django.urls import path
from django.conf.urls import url
from face_detect_app.views import ImageFaceDetect, LiveVideoFaceDetect

urlpatterns = [
    # path('video_feed/', views.video_feed, name='video_feed'),
    # path('camera/', views.camera, name='camera'),
    url(r'^face-detect/image/$', ImageFaceDetect.as_view(), name='image'),
    url(r'^face-detect/video/$', LiveVideoFaceDetect.as_view(), name='live_video'),
    # path('face-detect/video/', LiveVideoFaceDetect.as_view(), name='face-detect'),
]