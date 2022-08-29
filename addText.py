# from tkinter import image_names
from time import sleep
from PIL import Image, ImageFont, ImageDraw 
import os
# img = Image.open('img1.jpg')
# d1 = ImageDraw.Draw(img)
# w, h = img.size

# shape = [(w*0.1, h*0.8), (w*0.9, h)]
# d1.rectangle(shape, fill=(255,255,255))
# myFont = ImageFont.truetype('Roboto-Bold.ttf',size=50)
# d1.text((w*0.15, h*0.85), "Sample text", font=myFont, fill =(0, 0, 0))
# # d1.text((0, 0), "Sample text", fill =(255, 0, 0))

# # print(img.size)
# img.show()
# img.save("image1.jpg")

import csv

with open('courses.csv') as f:
    reader=csv.reader(f)

    for index, lines in enumerate(reader, start=1):
        imgName=lines[0]
        courseName=lines[1]

        # print('jpgImages/{}'.format(imgName))
        img = Image.open('jpgImages/{}'.format(imgName))
        d1 = ImageDraw.Draw(img)
        w, h = img.size
        print(img.size)

        shape = [(w*0.1, h*0.8), (w*0.9, h)]
        d1.rectangle(shape, fill=(255,255,255))
        sz=min((int)(h*0.05),(int)(w*0.05))
        sz=(int)(w*0.03)
        myFont = ImageFont.truetype('Roboto-Bold.ttf',size=sz)
        # print('{}'.format(courseName))
        d1.text((w*0.25, h*0.85), '{}'.format(courseName), font=myFont, fill =(0, 0, 0))
        s='newImages/'+str(index) + ' ' + courseName+'.jpeg'
        print(s)
        print(os.path.splitext(s))
        img.show()
        img.save(s,'jpeg')
        # sleep(10)




        