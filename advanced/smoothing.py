import cv2 as cv

img = cv.imread('../resources/Photos/park.jpg')
cv.imshow('img',img)

# averaging
average = cv.blur(img, (7,7))
cv.imshow('average', average)

# gaussian
gaussian = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('gaussian', gaussian)

# median
median = cv.medianBlur(img, 7)
cv.imshow('median', median)

# bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 35)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)