import cv2 as cv
img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

# averaging
average = cv.blur(img, (5,5))
cv.imshow('Average Blur', average) 

# gaussian blur
gaus_blur = cv.GaussianBlur(img, (3,3), 0)
cv.imshow("Gaussian Blur", gaus_blur)

#median blur
med_blur = cv.medianBlur(img, 5)
cv.imshow('Median Blur', med_blur)

#Bilaterl blur
bil_blur = cv.bilateralFilter(img, 10, 30, 30)
cv.imshow('Bilateral', bil_blur)


cv.waitKey(0)