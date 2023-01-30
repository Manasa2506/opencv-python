import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    # images videos and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img = cv.imread('Photos\cat.jpg')

resized_img = rescaleFrame(img)

cv.imshow('Cat', resized_img)

cv.waitKey(0)

#capture = cv.VideoCapture('Videos\dog.mp4')

# while True:
# isTrue, frame = capture.read()   # reads frame by frame

#frame_resized = rescaleFrame(frame)

#cv.imshow('Video', frame)
#cv.imshow('Video Resized', frame_resized)

# if cv.waitKey(20) & 0xFF == ord('d'):
# break

# capture.release()
# cv.destroyAllWindows()
