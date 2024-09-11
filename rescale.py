import cv2 as cv

img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Cat', img)


def rescale_frames(frame, scale=0.75):
    # Images, Videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescale_frames(frame, scale=0.2)
    cv.imshow('Video', frame)
    cv.imshow('Video resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

img_resized = rescale_frames(img)
cv.imshow('Cat Resized', img_resized)

cv.waitKey(0)

def changeRes(width, height):
    # Live video
    capture.set(3, width)
    capture.set(4,height)