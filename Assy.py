import os
import random
from tkinter import *
import vlc
import time
from PIL import Image, ImageTk
from datetime import datetime

def isVideo(cFilename):
    lVideoExtensions = ['.mp4', '.MP4', '.MOV', '.mov']
    fileName, fileEx = os.path.splitext(cFilename)
    return fileEx in lVideoExtensions

def isPhoto(cFilename):
    lPhotoExtensions = ['.JPG', '.JPEG', '.jpg', '.jpeg']
    fileName, fileEx = os.path.splitext(cFilename)
    return fileEx in lPhotoExtensions

def show_time_for_sec_on_canvas(canvas, iSec):
    hStart = datetime.now()

    # Show start time
    hTime = canvas.create_text(110, 75, text=hStart.strftime('%H:%M'), font = ("Helvetica", 50), fill = "white")
    hDate = canvas.create_text(110, 110, text=tWeekdayText[datetime.today().weekday()] + ', ' + tMonthText[hStart.month] + ' ' + str(hStart.day), font = ("Helvetica", 15), fill = "white")
    win.update()
    iScreenMinute = hStart.minute

    hEnd = datetime.now()
    while (hEnd - hStart).total_seconds() < iSec:
        if(hEnd.minute != iScreenMinute):
            canvas.delete(hTime)
            canvas.delete(hDate)

            # Update Date in Screen
            hTime = canvas.create_text(110, 75, text=hEnd.strftime('%H:%M'), font = ("Helvetica", 50), fill = "white")
            hDate = canvas.create_text(110, 110, text=tWeekdayText[datetime.today().weekday()] + ', ' + tMonthText[hEnd.month] + ' ' + str(hEnd.day), font = ("Helvetica", 15), fill = "white")
            win.update()

            iScreenMinute = hEnd.minute
        time.sleep(1)
        hEnd = datetime.now()
    canvas.delete(hTime)
    canvas.delete(hDate)


cBaseDir = '/media/rgweon/rhgweon/photo/' # base directory
lFiles = os.listdir(cBaseDir) # file list
tImgPos = (640, 360)

tMonthText = ('None', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
tWeekdayText = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')

# Create Base Window
win = Tk()
win.geometry('1280x720')
win.configure(bg='black')
win.title('A-rin')

# Create Frame and Canvas for video and photo
'''
hMediaFrame = Frame(win, width=1280, height=720, background='black')
hCanvas = Canvas(hMediaFrame, background='black')
hCanvas.config(bd=0, highlightthickness=0)
hCanvas.pack(fill=BOTH, expand=1)
hMediaFrame.pack(fill=BOTH, expand=1)
'''

# Create vlc media player
hVlc = vlc.Instance()
hMediaPlayer = hVlc.media_player_new()

win.update()

while True:
    # Choose a random file
    cTargetFile = random.choice(lFiles)
    print(cTargetFile)

    if isVideo(cTargetFile):
        hLeftCanvas = Canvas(win, background='black')
        hLeftCanvas.config(width=200, height=720, bd=0, highlightthickness=0)
        hLeftCanvas.grid(column=0, row=0)

        hMediaFrame = Frame(win, width=880, height=720, background='black')
        hMediaFrame.grid(column=1, row=0)
        hMediaPlayer.set_xwindow(hMediaFrame.winfo_id())

        hRightCanvas = Canvas(win, background='black')
        hRightCanvas.config(width=200, height=720, bd=0, highlightthickness=0)
        hRightCanvas.grid(column=2, row=0)


        hMediaFile = hVlc.media_new(os.path.join(cBaseDir, cTargetFile))
        hMediaPlayer.set_media(hMediaFile)
        hMediaPlayer.play()
        hMediaPlayer.audio_set_volume(0)
        win.update()

        show_time_for_sec_on_canvas(hLeftCanvas, 2)
        hMediaPlayer.audio_set_volume(0)
        show_time_for_sec_on_canvas(hLeftCanvas, hMediaPlayer.get_length()/1000)

        hMediaPlayer.stop()
        hLeftCanvas.destroy()
        hMediaFrame.destroy()
        hRightCanvas.destroy()

    elif isPhoto(cTargetFile):
        hPhotoCanvas = Canvas(win, background='black')
        hPhotoCanvas.config(width=1280, height=720, bd=0, highlightthickness=0)
        hPhotoCanvas.grid(column=0, row=0)

        # Show Target photo
        hImg = Image.open(os.path.join(cBaseDir, cTargetFile))
        hImg.thumbnail((1280, 720), Image.ANTIALIAS)
        hImg = ImageTk.PhotoImage(hImg, master=win)
        hPhoto = hPhotoCanvas.create_image(tImgPos, image=hImg)

        # Show Date and Time
        show_time_for_sec_on_canvas(hPhotoCanvas, 5)

        time.sleep(5)
        hPhotoCanvas.destroy()
    else:
        print(f'cannot play {cTargetFile}')

win.mainloop()
