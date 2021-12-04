import cv2 as cv
# img = cv.imread('Photos/cat_large.jpg')


def rescaleFrame(frame, scale=0.75):
    # for images, videos, live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# resized_image = rescaleFrame(img, scale=0.5)
# cv.imshow('Resized Image', resized_image)
# cv.imshow('Cat', img)
capture = cv.VideoCapture('Videos/dog.mp4')


while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=0.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
# cv.waitKey(0)  ## for image