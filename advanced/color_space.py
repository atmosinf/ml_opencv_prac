import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('../resources/Photos/park.jpg')
cv.imshow('img',img)

# BGR to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grey', gray)

# BGR to HSV - hue saturation value
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

#BGR to lab
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)
plt.imshow(rgb)
plt.show()

cv.waitKey(0)
