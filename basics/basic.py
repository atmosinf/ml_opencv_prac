import cv2 as cv

img = cv.imread('Photos/park.jpg')
cv.imshow('boston',img)

# converting to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# blur an image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

# edge cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('canny',canny)

# dilating an image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('dilated',dilated)


cv.waitKey(0)