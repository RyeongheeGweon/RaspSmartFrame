import os
import random
from tkinter import *
import vlc
import time
from PIL import Image, ImageTk

def isVideo(cFilename):
    lVideoExtensions = ['.mp4', '.MP4', '.MOV', '.mov']
    fileName, fileEx = os.path.splitext(cFilename)
    return fileEx in lVideoExtensions

def isPhoto(cFilename):
    lPhotoExtensions = ['.JPG', '.JPEG', '.jpg', '.jpeg']
    fileName, fileEx = os.path.splitext(cFilename)
    return fileEx in lPhotoExtensions


cBaseDir = '/media/rgweon/rhgweon/photo/' # base directory
lFiles = os.listdir(cBaseDir) # file list
tImgPos = (640, 360)

# Create Base Window
win = Tk()
win.geometry('1280x720')
win.title('A-rin')

# Create Frame and Canvas for video and photo
hMediaFrame = Frame(win, width=1280, height=720, background='black')
hCanvas = Canvas(hMediaFrame, background='black')
hCanvas.config(bd=0, highlightthickness=0)
hCanvas.pack(fill=BOTH, expand=1)
hMediaFrame.pack(fill=BOTH, expand=1)

# Create vlc media player
hVlc = vlc.Instance()
hMediaPlayer = hVlc.media_player_new()
hMediaPlayer.set_xwindow(hMediaFrame.winfo_id())

win.update()

while True:
    # Choose a random file
    cTargetFile = random.choice(lFiles)
    print(cTargetFile)

    if isVideo(cTargetFile):
        hMediaFile = hVlc.media_new(os.path.join(cBaseDir, cTargetFile))
        hMediaPlayer.set_media(hMediaFile)
        hMediaPlayer.play()
        hMediaPlayer.audio_set_volume(0)
        win.update()

        time.sleep(2)
        hMediaPlayer.audio_set_volume(0)
        time.sleep(hMediaPlayer.get_length()/1000)
        hMediaPlayer.stop()
    elif isPhoto(cTargetFile):
        hImg = Image.open(os.path.join(cBaseDir, cTargetFile))
        hImg.thumbnail((1280, 720), Image.ANTIALIAS)
        hImg = ImageTk.PhotoImage(hImg, master=win)
        hPhoto = hCanvas.create_image(tImgPos, image=hImg)
        win.update()

        time.sleep(5)
        hCanvas.delete(hPhoto)
    else:
        print(f'cannot play {cTargetFile}')

win.mainloop()
