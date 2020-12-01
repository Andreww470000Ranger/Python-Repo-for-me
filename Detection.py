# -*- coding: utf-8 -*-

"""
Created on Mon Nov 23 13:22:21 2020

@author: ricardo.montoya
"""

import cv2 as cv

img = cv.imread("Photos/cat.jpg")

cv.imshow('Cat', img)

capture = cv.VideoCapture(0)

def changeRes(width, height):
    capture.set(2, width)
    capture.set(4, height)
    
    

def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video Resized', frame_resized)
    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()