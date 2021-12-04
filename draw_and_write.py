import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)
# img = cv.imread('Photos/cat.jpg')
# cv.imshow('Cat', img)

## paint the entire image

blank[:] = 0,255,0
cv.imshow('Green', blank)
blank[:] = 0,0,255
cv.imshow('Red', blank)

## coloring a certain part of image

blank[200:300, 300:400] = 0,255,0
cv.imshow('Green_certain', blank)

## drawing shapes
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow('Rectangle', blank)

cv.circle(blank, (250,250), 50, (0,0,255), thickness=-1)
cv.imshow("Circle",blank)

cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
cv.imshow("Line", blank)


## text on image
cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow("Text",blank)


cv.waitKey(0)