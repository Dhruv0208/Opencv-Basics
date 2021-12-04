import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Original', img)

## Translation

def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, transMat, dimensions)

## -x --> left
## -y --> up
## x --> right
## y --> down

translated = translate(img, -100,100)
cv.imshow('Translated', translated)

## Rotations
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45) #positive value --> anti-clockwise and vice-versa
cv.imshow('Rotated', rotated)

## Flipping

flipped = cv.flip(img, -1) #0--> verticall, 1-->horizontally, -1-->both
cv.imshow('Flipped', flipped)

cv.waitKey(0)