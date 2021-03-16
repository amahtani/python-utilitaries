# usage : python3 split_reduce_save.py -v Nako1.mp4 -fps 1

import cv2
#import numpy as np
import os
import sys
import argparse

a = argparse.ArgumentParser()
a.add_argument("-v", "--video", help="path to video")
a.add_argument('-fps', help="FPS of the output video", default = 10)
args = a.parse_args()
print(args)

try:
    if not os.path.exists('data'): # if folder named data does not exist
        os.makedirs('data') # create a data folder
except OSError:
    print ('Error: Creating directory of data')

# Playing video from file:
cap = cv2.VideoCapture(args.video)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
out = cv2.VideoWriter(args.video+'_out.avi',cv2.VideoWriter_fourcc('M','J','P','G'), int(args.fps), (frame_width,frame_height))

def getFrame(sec):
    cap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = cap.read()
    if hasFrames:
        # Saves image of the current frame in jpg file
        name = './data/' + args.video[:-4] + "_" + 'frame' + str(count) + '.jpg'
        print ('Creating...' + name)
        cv2.imwrite(name, image)
        out.write(image)
    return hasFrames


sec = 0
frameRate = int(args.fps)
count=1
success = getFrame(sec)

while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)


