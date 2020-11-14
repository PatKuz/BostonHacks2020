'''
Opens a webcam window, and awaits user to input 'q'.

Saves a screenshot in running dir and closes
'''
import cv2
import time

camera = cv2.VideoCapture(0)
lastCapture = time.time()

def checkImg(curTime):
    if(time.time() - curTime > 1):
        cv2.imwrite('test.jpg',image)
        lastCapture = time.time()

while True:
    return_value,image = camera.read()
    cv2.imshow('image',image) 
    checkImg(lastCapture)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

camera.release()
cv2.destroyAllWindows()