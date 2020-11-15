from webcam_capture import getVideoFrame
from send_sms import send_message
from evaluation import get_prediction
from drawRect import drawRect
import time

#starts webcam and begins implicit screenshot capture
#to screenshot folder
getVideoFrame()

'''
 - passes frame to trained ML model and returns guess, if mask is detected,
   sends message to client and sleeps the guessing loop for 30 seconds.
   Moves the photo that is detected immediately to a holding folder.
'''
