import cv2 as cv
# Reading Images

img = cv.imread('Resources/Photos/cats.jpg')

cv.imshow('Cat', img)

# Averaging
average = cv.blur(img, (7,7))
cv.imshow('Average', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian', gauss)

# Median Blur
median = cv.medianBlur(img, 7)
cv.imshow('Median', median)

#Bilateral
bilateral = cv.bilateralFilter(img, 15, 35, 25)
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)