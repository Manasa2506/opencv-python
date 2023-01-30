import cv2 as cv

# importing images
img = cv.imread('Photos\cat.jpg')

cv.imshow('Cat', img)

cv.waitKey(0)

# import videos-webcam using 0

#capture = cv.VideoCapture(0)
#capture.set(3, 640)
#capture.set(4, 480)
#capture.set(10, 100)

# while True:
# isTrue, frame = capture.read()  # reads frame by frame
#cv.imshow('Video', frame)

# if cv.waitKey(20) & 0xFF == ord('d'):
# break

# capture.release()
# cv.destroyAllWindows()
