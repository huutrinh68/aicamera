from django.shortcuts import render, redirect
from django.http.response import HttpResponse, StreamingHttpResponse
from datetime import datetime
import cv2
from .camera import VideoCamera

# Create your views here.
webcam_id = 0

def gen_camera(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feed(request):
    d = {
        'hour': datetime.now().hour,
        'message': 'Hello'
    }
    redirect('/video_feed/')
    # return render(request, 'index.html', d)
    frame = gen_camera(VideoCamera(0))
    return StreamingHttpResponse(frame, content_type='multipart/x-mixed-replace; boundary=frame')
