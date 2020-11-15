import numpy as np
import cv2, time, yaml
import tkinter as tk
from PIL import Image, ImageTk
from evaluation import get_prediction
from drawRect import drawRect
from send_sms import send_message

'''
evalTimer - used to measure elapsed time since last sent message
lastCapture - used to measure elapsed time since last frame evaluation
message_sent - tracks if a text message has been sent in the last 15 seconds
'''
evalTimer = time.time()
lastCapture = time.time()
message_sent = False

#Set up GUI
window = tk.Tk()  #Makes main window
window.wm_title("BHACKS 2020 Mask")
window.config(background="#312a2a")

#Graphics window
imageFrame = tk.Frame(window, width=600, height=500)
imageFrame.grid(row=0, column=0, padx=10, pady=2)

'''
checkEvalTime - checks if 15 seconds have elapsed from last text sent, if yes,
sets global message_sent to false and resets timer. If no message sent in last 15 seconds, breaks
'''
def checkEvalTime():
    global evalTimer, message_sent
    curTime = time.time()

    if(message_sent and curTime - evalTimer > 15):
        message_sent = False
        evalTimer = time.time()


'''
checkEval - image (OpenCV) - opens credentials with phone number destination and twilio auth tokens.
Passes openCv image, writes it to local dir, and passes it through AutoML trained for mask states.
If conditions are met, will text alert to user based on the detected mask state.
'''
def checkEval(image):
    creds = yaml.safe_load(open("creds.yaml", "r"))
    toNum = creds['to']
    #overwrites the previous image captured
    cv2.imwrite('Active_Captures/frame.jpg', image)
    label, x1, y1, x2, y2 = get_prediction('Active_Captures/frame.jpg')
    global message_sent
    if label != None and label != 'mask':
        if (message_sent == False):
            img = drawRect('Active_Captures/frame.jpg', label, x1, y1, x2, y2)
            if label == 'improper_mask':
                msg = 'Improper Mask Detected: Better get that mask over your nose!'
                send_message(msg, toNum=toNum, image=img)
                message_sent = True
                evalTimer = time.time()
            else:
                msg = 'No Mask Detected: STOP! You need your mask!'
                send_message(msg, toNum=toNum, image=img)
                message_sent = True
                evalTimer = time.time()

#Capture video frames
lmain = tk.Label(imageFrame)
lmain.grid(row=0, column=0)
#initializes video feed w/ OpenCV
cap = cv2.VideoCapture(0)

'''
show_frame - displays frame to the Tkinter gui window. If 2 seconds have passed,
passes current frame to be evaluated by AutoML.
'''
def show_frame():
    try:
        global lastCapture, evalTimer
        _, frame = cap.read()
        cv2image = cv2.flip(frame, 1)

        checkEvalTime()
        if(message_sent == False):
            evalTimer = time.time()

        #cv2 image is the frame we want to analyze
        #only saves img and analyzes every 2 seconds
        if time.time() - lastCapture > 2:
                checkEval(cv2image)
                lastCapture = time.time()

        img = Image.fromarray(cv2image)
        r, g, b = img.split()
        img = Image.merge('RGB', (b, g, r))
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(10, show_frame)
    except KeyboardInterrupt:
        window.destroy()
        cap.release()
        cv2.destroyAllWindows()


#Slider window (slider controls stage position)
sliderFrame = tk.Frame(window, width=600, height=100)
sliderFrame.grid(row = 600, column=0, padx=10, pady=2)


show_frame()  #Display 2
window.mainloop()  #Starts GUI
