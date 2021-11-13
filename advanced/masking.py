import cv2 as cv
import numpy as np

img = cv.imread('../resources/Photos/cats.jpg')
cv.imshow('img',img)

blank = np.zeros(img.shape[:2], dtype='uint8')
# cv.imshow('blank',blank)

mask = cv.rectangle(blank, (30,30), (200,200), 255, -1)
# cv.imshow('mask', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('masked image', masked)


cv.waitKey(0)