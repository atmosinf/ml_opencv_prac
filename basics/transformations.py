import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('boston',img)

# translation 
def translate(img, x, y):
    transmat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, transmat, dimensions)

translated = translate(img, 100, 100)
cv.imshow('translated', translated)

# rotate
def rotate(img, angle, rotpoint=None):
    (height, width) = img.shape[:2]

    if rotpoint is None:
        rotpoint = (width//2, height//2)

    rotmat = cv.getRotationMatrix2D(rotpoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotmat, dimensions)

rotated = rotate(img, 45)
cv.imshow('rotated', rotated)

# resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

# flip
flipped = cv.flip(img, -1)
cv.imshow('flipped', flipped)


cv.waitKey(0)