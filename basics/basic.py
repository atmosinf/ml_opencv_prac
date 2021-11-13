import cv2 as cv

img = cv.imread('Photos/park.jpg')
cv.imshow('boston',img)

# converting to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# blur an image



cv.waitKey(0)