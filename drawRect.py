from PIL import Image, ImageDraw
from datetime import datetime

'''
drawRect - draws a labeled rectangle on an image given the filepath, label, and coordinates of
top left and bottom right veritces
'''
def drawRect(file_path,label,x1,y1,x2,y2):
    im = Image.open(file_path)
    draw = ImageDraw.Draw(im)
    vertices = ((x1*1280,y1*720),(x1*1280,y2*720),(x2*1280,y2*720),(x2*1280,y1*720))
    draw.polygon(vertices,fill=None,outline=(0,255,255))
    draw.text((x1*1280,y1*720), label)
    im.save('Archived/bounded_frame.jpg', quality=95)
    return 'Archived/bounded_frame.jpg'
