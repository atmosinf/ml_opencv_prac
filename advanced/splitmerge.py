import cv2 as cv

img = cv.imread('../resources/Photos/park.jpg')
cv.imshow('img',img)

b,g,r = cv.split(img)
cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('red',r)

cv.waitKey(0)