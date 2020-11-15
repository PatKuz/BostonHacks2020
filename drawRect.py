from PIL import Image, ImageDraw
from datetime import datetime

'''
drawRect - draws a labeled rectangle on an image given the filepath, label, and coordinates of
top left and bottom right veritces
'''
def drawRect(file_path,label,x1,y1,x2,y2):
    im = Image.open(file_path)
    draw = ImageDraw.Draw(im)
    vertices = ((x1*640,y1*480),(x1*640,y2*480),(x2*640,y2*480),(x2*640,y1*480))
    draw.polygon(vertices,fill=None,outline=(0,255,255))
    draw.text((x1*640,y1*480), label)
    im.save('Archived/bounded_frame.jpg', quality=95)
    return 'Archived/bounded_frame.jpg'