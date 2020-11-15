from PIL import Image, ImageDraw
from datetime import datetime

def drawRect(file_path,label,x1,y1,x2,y2):
    im = Image.open(file_path)
    draw = ImageDraw.Draw(im)
    vertices = ((x1*1080,y1*720),(x1*1080,y2*720),(x2*1080,y2*720),(x2*1080,y1*720))
    draw.polygon(vertices,fill=None,outline=(0,255,255))
    draw.text((x1*1080,y1*720), label)
    im.save('Archived/'+ str(datetime.now().strftime("%H%M%S"))+'.jpg', quality=95)
    return 'Archived/'+ str(datetime.now().strftime("%H%M%S"))+'.jpg'
