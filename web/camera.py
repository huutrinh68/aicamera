import cv2 

class VideoCamera(object):
    def __init__(self, camera_id=None):
        if camera_id is not None:
            self.camera_id = camera_id
        else:
            self.camera_id = 0
        self.video = cv2.VideoCapture(self.camera_id)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        image = cv2.flip(image, 1)
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.

        _, jpgeg = cv2.imencode('.jpg', image)
        return jpgeg.tobytes()
        
        