# Usage : python split.py -v 2.mp4 --skip 100


import cv2
import numpy as np
import os
import sys
import argparse

a = argparse.ArgumentParser()
a.add_argument("-v", "--video", help="path to video")
a.add_argument('--skip', help="Only save every nth frame", default = 1)
a.add_argument('--mirror', action='store_true', help="Flip every other image", default = False)
args = a.parse_args()
print(args)

skip = int(args.skip)
mirror = bool(args.mirror)

# Playing video from file:
cap = cv2.VideoCapture(args.video)

try:
    if not os.path.exists('data'): # if folder named data does not exist
        os.makedirs('data') # create a data folder
except OSError:
    print ('Error: Creating directory of data')

index = 0
last_mirrored = True
currentFrame = 0
while(True):

    cap.set(cv2.CAP_PROP_POS_MSEC,(currentFrame*1000)) 
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret:
        if index % skip == 0:
            if args.mirror and last_mirrored:
                frame = np.fliplr(frame)
                last_mirrored = not last_mirrored

        # Saves image of the current frame in jpg file
        name = './data/' + args.video[:-4] + "_" + 'frame' + str(currentFrame) + '.jpg'
        print ('Creating...' + name)
        cv2.imwrite(name, frame)

        # To stop duplicate images
        currentFrame += 1

    else:
        break
    index += 1    

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()