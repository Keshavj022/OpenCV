import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')

cv.imshow('Blank', blank)

# 1. Point the image a certain color
blank[:] = 0,255,0
cv.imshow('Green', blank)

blank[:] = 0,0,255
cv.imshow('Red', blank)

blank[200:300, 300:400] = 0,255,0
cv.imshow('Green Square', blank)

# 2. Draw a Rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=cv.FILLED)
cv.imshow("Green Rectangle", blank)

cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)
cv.imshow("Green Rectangle", blank)

cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=-1)
cv.imshow("Green Rectangle", blank)

cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=3)
cv.imshow("Green Rectangle", blank)

# 3. Draw a Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2),40,(0,0,255), thickness=3 )
cv.imshow("Red Circle", blank)

# 4. Draw a Line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
cv.imshow("line", blank)

# 5. Write text on image
cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, fontScale=1.0, color=(0,255,0), thickness=2)
cv.imshow('Text', blank)

cv.waitKey(0)