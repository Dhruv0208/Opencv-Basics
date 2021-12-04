import cv2 as cv

img = cv.imread('Photos/park.jpg')
cv.imshow("Original", img)

## color conversion
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("GrayScale", gray)

## blurring
blurred = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow("Blurred", blurred)

## Edge cascade
canny_edge = cv.Canny(blurred, 125, 175) ## 'img' for the most edges and 'blurred' to reduce the number of edges
cv.imshow('Edges', canny_edge)

## dilating image: bsically increasing thickness of images or zooming
dilated = cv.dilate(canny_edge, (3,3), iterations=3)
cv.imshow('Dilated', dilated)

## erosing image: reverse of dilating
erroded = cv.erode(dilated, (3,3), iterations=3)
cv.imshow('Erroded', erroded)

## resizing using cv.resize
resized = cv.resize(img, (300,300), interpolation=cv.INTER_AREA)
cv.imshow("Resized", resized)

## cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)