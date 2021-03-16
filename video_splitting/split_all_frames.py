# Usage : python split.py -v 2.mp4 --skip 100


import cv2
import numpy as np
import os
import sys
import argparse

a = argparse.ArgumentParser()
a.add_argument("-v", "--video", help="path to video")
args = a.parse_args()
print(args)

# Playing video from file:
cap = cv2.VideoCapture(args.video)

try:
    if not os.path.exists('data'): # if folder named data does not exist
        os.makedirs('data') # create a data folder
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
while(True):

    cap.set(cv2.CAP_PROP_POS_MSEC,(currentFrame*1000)) 
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Saves image of the current frame in jpg file
    name = './data/' + args.video[:-4] + "_" + 'frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()