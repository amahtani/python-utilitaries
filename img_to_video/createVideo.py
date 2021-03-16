# Usage : python createVideo.py --p img_folder/ --w 640 --h 480 --fps 10

import cv2
import numpy as np
import glob
import sys
import argparse
 
a = argparse.ArgumentParser()
a.add_argument("--path", help="path images folder")
a.add_argument('--fps', help="number of FPS desired", default = 0.5)
a.add_argument('--w', help="width of input", default = 1920)
a.add_argument('--h', help="height of input", default = 1080)
args = a.parse_args()
print(args)

img_array = []
for filename in glob.glob(args.path + '/*.png'):

    if (len(glob.glob(args.path + '/*.png')) == 0) : 
        print("no image in folder or worong folder") 
    img = cv2.imread(filename)
    img_array.append(img)


out = cv2.VideoWriter('compil.avi',cv2.VideoWriter_fourcc(*'MPEG'), int(args.fps), (int(args.w), int(args.h)))
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
