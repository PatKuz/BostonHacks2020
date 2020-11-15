'''
Opens a webcam window, and awaits user to input 'q' to quit.
|
Saves a screenshot every half second in running dir
'''
import cv2, time
from evaluation import get_prediction
from drawRect import drawRect
from send_sms import send_message


camera = cv2.VideoCapture(0)

#method to check if a second has passed
def checkEval(image):
    #overwrites the previous image captured
    cv2.imwrite('Active_Captures/frame.jpg',image)
    label,x1,y1,x2,y2 = get_prediction('Active_Captures/frame.jpg')
    if label != None and label!='mask':
        img = drawRect('Active_Captures/frame.jpg',label,x1,y1,x2,y2)
        if label=='improper_mask':
            msg = 'Improper Mask Detected: Better get that mask over your nose!'
        else:
            msg = 'No Mask Detected: STOP! You need your mask!'
        send_message(msg,toNum="+14845385080",image=img)
        time.sleep(5)

def getVideoFrame():
    lastCapture = time.time()
    while(1):
        return_value,image = camera.read()
        if time.time() - lastCapture > 2:
            checkEval(image)
            lastCapture = time.time()

    camera.release()
    cv2.destroyAllWindows()

getVideoFrame()
