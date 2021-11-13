import cv2 as cv

img = cv.imread('../resources/Photos/park.jpg')
cv.imshow('img',img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])
cv.imshow('blue',blue)
cv.imshow('green',green)
cv.imshow('red',red)

# cv.imshow('blue',b)
# cv.imshow('green',g)
# cv.imshow('red',r)

merged = cv.merge([b,g,r])
cv.imshow('merged',merged)

cv.waitKey(0)