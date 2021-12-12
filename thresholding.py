import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# simple thresholding
threshold, thresh = cv.threshold(gray, 105, 255, cv.THRESH_BINARY)
cv.imshow('Thresholded', thresh)

#inverse threshold
threshold, thresh_inv = cv.threshold(gray, 105, 255, cv.THRESH_BINARY_INV)
cv.imshow('Thresholded INVERSE', thresh_inv)

#adaptive threshold
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, 
cv.THRESH_BINARY, 11, 9)
cv.imshow('Adaptive', adaptive_thresh)

cv.waitKey(0)