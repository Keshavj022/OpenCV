import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/Park.jpg')

cv.imshow('Park', img)

# Translation

# -x --> left
# -y --> up
# x --> right
# y --> down

def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


translated = translate(img, 200, 100)
cv.imshow('Translated', translated)

# Rotation

# angle --> anti-clockwise
# -angle --> clockwise

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('rotated', rotated)

rotated_rotated = rotate(rotated, 45)
cv.imshow('rotated-rotated', rotated_rotated)

# Resizing

resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('bigresized', resized)

resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('smallresized', resized)

# Flipping

# 0 --> vertical flip
# 1 --> horizontal flip
# -1 --> vertical and horizontal flip

flip = cv.flip(img, 1)
cv.imshow('flipped', flip)

# Cropping

cropped = img[200:400, 300:400]
cv.imshow('croped', cropped)

cv.waitKey(0)