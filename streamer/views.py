from django.shortcuts import render, redirect
from django.http.response import HttpResponse, StreamingHttpResponse
from datetime import datetime
import cv2
from streamer.camera import VideoCamera

from django.utils.safestring import mark_safe
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# Create your views here.
webcam_id = 0

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feed(request):
    redirect('/video_feed/')
    frame = gen(VideoCamera(0))
    # layer = get_channel_layer()
    # group_name = 'streamer'

    # async_to_sync(layer.group_send)(
    #         group_name,
    #         {
    #             'type': 'update.frame',
    #             'data': frame
    #         }
    # )

    return StreamingHttpResponse(frame, content_type='multipart/x-mixed-replace; boundary=frame')

def camera(request):
    return render(request, 'streamer.html')