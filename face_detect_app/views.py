from django.shortcuts import render, redirect
from django.http.response import HttpResponse, StreamingHttpResponse
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.views.generic import TemplateView

from face_detect_app.camera import VideoCamera
from face_detect_app.detect import get_face_detect_data

# Create your views here.
# webcam_id = 0

# def gen(camera):
#     while True:
#         frame = camera.get_frame()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# def video_feed(request):
#     redirect('/video_feed/')
#     frame = gen(VideoCamera(0))

#     return StreamingHttpResponse(frame, content_type='multipart/x-mixed-replace; boundary=frame')

# def camera(request):
#     return render(request, 'streamer.html')


def upload_file(image):
    fs = FileSystemStorage()
    filename = fs.save(image.name, image)
    uploaded_file_url = fs.path(filename)
    return uploaded_file_url


class ImageFaceDetect(TemplateView):
    template_name = 'image.html'

    def post(self, request, *args, **kwargs):
        data = request.POST.get('image')
        try:
            image_data = get_face_detect_data(data)
            if image_data:
                return JsonResponse(status=200, data={'image': image_data.decode(), 'message': 'Face detected'})
        except Exception as e:
            print(e)
            pass
        return JsonResponse(status=400, data={'errors': {'error_message': 'No face detected'}})


class LiveVideoFaceDetect(TemplateView):
    template_name = 'video.html'

    def post(self, request, *args, **kwargs):
        return JsonResponse(status=200, data={'message': 'Face detected'})