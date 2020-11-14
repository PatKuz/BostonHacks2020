'''
Opens a webcam window, and awaits user to input 's'.

Saves a screenshot in running dir and closes
'''

import cv2
camera = cv2.VideoCapture(0)
while True:
    return_value,image = camera.read()
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow('image',gray)
    if cv2.waitKey(1)& 0xFF == ord('s'):
        cv2.imwrite('test.jpg',image)
        break
camera.release()
cv2.destroyAllWindows()