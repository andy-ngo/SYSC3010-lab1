from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 30

#retuns camera instance
def get_camera():
    return camera
    
#Takes in camera instance and preview time
#displays camera preview for the indicated amount of time
def camera_preview(camera, preview_time):
    camera.start_preview()
    sleep(preview_time)
    camera.stop_preview()
    
#Takes in camera instance and degrees
#rotates camera to the indicated degree
def rotate_camera(Camera,degrees):
    camera.rotation = degrees
    
#Takes in camera instance, output image location, countdown time and preview Boolean
#If preview is trye, preview is started
#the code waits the indicated countdown time before the image is taken and stored in the
#indicated location
#the preview is stopped if it was started
def capture_image(camera, image_out_location, countdown_time = 0, preview = False):
    if preview is True:
        camera.start_preview()
        
    sleep(countdown_time)
    camera.capture(image_out_location)
    camera.stop_preview()
    
#Takes in camera instance, output video location, video length, countdown time and preview
#Boolean
#If preview is true, preview is started
#The code waits the indicate countdown time before the video is taken for hte indicated amount
#of time
#and stored in the indicated location
#the preview is stopped if it was started
def capture_video(camera,video_out_location,video_length,countdown_time = 0, preview = False): 
    if preview is True:
        camera.start_preview()
        
    camera.start_recording(video_out_location)
    sleep(video_length)
    camera.stop_recording()
    camera.stop_preview()