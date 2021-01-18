# -*- coding: utf-8 -*-
"""
Spyder Editor

Get video and play in a video box

usage: q to quit or wait until video finish

Put the name of the video in the text file

"""

import numpy as np
import cv2

resizeFactor = .5;

cv2.namedWindow("original / output", cv2.WINDOW_KEEPRATIO)
cv2.moveWindow("original / output", 40,30)

# load filename
file1 = open('filename.txt', 'r') 

Lines = [line.rstrip('\n') for line in file1]

cap = cv2.VideoCapture(Lines[0])

ret, frame = cap.read()
height, width = frame.shape[:2]
newH = int(height * resizeFactor)
newW = int(width * resizeFactor)

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_3_channel = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        gray_stack = np.hstack((frame, gray_3_channel))

        cv2.imshow('original / output', gray_stack)

        cv2.resizeWindow('original / output', newW, newH)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()