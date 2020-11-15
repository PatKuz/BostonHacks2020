import numpy as np
import cv2
import tkinter as tk
from PIL import Image, ImageTk
import cv2
import time
from evaluation import get_prediction
from drawRect import drawRect
from send_sms import send_message

#Set up GUI
window = tk.Tk()  #Makes main window
window.wm_title("BHACKS 2020 Mask")
window.config(background="#FFFFFF")

#Graphics window
imageFrame = tk.Frame(window, width=600, height=500)
imageFrame.grid(row=0, column=0, padx=10, pady=2)

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

#Capture video frames
lmain = tk.Label(imageFrame)
lmain.grid(row=0, column=0)
cap = cv2.VideoCapture(0)

def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

    #cv2 image is the frame we want to analyze
    checkEval(cv2image)

    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame) 


#Slider window (slider controls stage position)
sliderFrame = tk.Frame(window, width=600, height=100)
sliderFrame.grid(row = 600, column=0, padx=10, pady=2)


show_frame()  #Display 2
window.mainloop()  #Starts GUI