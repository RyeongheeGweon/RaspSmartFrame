from tkinter import *
import vlc
import time
from PIL import Image, ImageTk

win = Tk()
win.geometry('1280x720')
win.configure(bg='black')
win.title('A-rin')

# Create vlc Instance, media player, open a file
vlcInstance = vlc.Instance()
mediaFile = vlcInstance.media_new("/media/rgweon/rhgweon/photo/IMG_3650.mp4")
mediaPlayer = vlcInstance.media_player_new()

# Create Frame for video

leftCanvas = Canvas(win, background='black')
leftCanvas.config(width=200, height=720, bd=0, highlightthickness=0)
leftCanvas.grid(column=0, row=0)

mediaFrame = Frame(win, width=880, height=720, background='black')
mediaFrame.grid(column=1, row=0)

rightCanvas = Canvas(win, background='black')
rightCanvas.config(width=200, height=720, bd=0, highlightthickness=0)
rightCanvas.grid(column=2, row=0)

hTime = leftCanvas.create_text(110, 75, text="11:30", font = ("Helvetica", 50), fill = "white")
hTime = leftCanvas.create_text(110, 110, text="Sat, Aug 27", font = ("Helvetica", 15), fill = "white")


# Set media
mediaPlayer.set_xwindow(mediaFrame.winfo_id())
mediaPlayer.set_media(mediaFile)
mediaPlayer.play()

tValue = mediaPlayer.video_get_size()
print(tValue)


win.update()
# time.sleep(mediaPlayer.get_length()/1000)
time.sleep(5)

mediaPlayer.stop()

leftCanvas.destroy()
mediaFrame.destroy()
rightCanvas.destroy()
'''
for wg in win.grid_slaves():
    wg.destroy()
'''

photoCanvas = Canvas(win, background='black')
photoCanvas.config(width=1280, height=720, bd=0, highlightthickness=0)
photoCanvas.grid(column=0, row=0)

img_pos = (640, 360)
img = Image.open("/media/rgweon/rhgweon/photo/IMG_3326.JPG")
img.thumbnail((1280, 720), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img, master = win)
photo = photoCanvas.create_image(img_pos, image=img)


win.mainloop()

"""
img_pos = (640, 360)
img = Image.open("/media/rgweon/rhgweon/photo/IMG_3326.JPG")
img.thumbnail((1280, 720), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img, master = win)
photo = canvas.create_image(img_pos, image=img)

win.update()
"""
