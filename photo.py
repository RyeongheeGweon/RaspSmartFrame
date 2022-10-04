from tkinter import *
from PIL import Image, ImageTk
import time

win = Tk()
win.geometry('1920x1080')

#Canvas
cvs = Canvas(win)
cvs.config(width=1920, height=1080, bd=0, highlightthickness=0)
cvs.configure(background='black')
cvs.pack()

img_pos = (960, 540)
img = Image.open("/media/rgweon/rhgweon/photo/IMG_3326.JPG")
img.thumbnail((1920, 1080), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img, master = win)
cvs.create_image(img_pos, image=img)

win.mainloop()
