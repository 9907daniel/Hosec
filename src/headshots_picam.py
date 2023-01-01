import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray
import sys
import uuid

name = sys.argv[1] # name passed from command line argument

cam = PiCamera()
cam.resolution = (512, 304)
cam.framerate = 10
rawCapture = PiRGBArray(cam, size=(512, 304))

while True:
    for frame in cam.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        cv2.imshow("Press Space to take a photo", image)
        rawCapture.truncate(0)
    
        k = cv2.waitKey(1)
        rawCapture.truncate(0)
        if k%256 == 27: 
            # ESC pressed
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "dataset/{}/image_{}.jpg".format(name, uuid.uuid4().hex)
            cv2.imwrite(img_name, image)
            print("{} written!".format(img_name))
            
    if k%256 == 27:
        print("Escape hit, closing...")
        break

cv2.destroyAllWindows()
