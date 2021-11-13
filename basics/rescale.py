import cv2 as cv

img = cv.imread('Photos/cat_large.jpg')

def rescaleframe(frame, scale=0.75):
    #works for images, video and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeres(width, height):
    #live video
    capture.set(3,width)
    capture.set(4,height)

resized_image = rescaleframe(img, 0.5)
cv.imshow('resized', resized_image)

capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleframe(frame, scale=0.2)
    
    cv.imshow('video', frame)
    cv.imshow('video resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()