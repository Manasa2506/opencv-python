import cv2 as cv
import numpy as np

img = cv.imread('Photos\park.jpg')

cv.imshow('Park', img)

# Translation
# -x --> left       x --> right
# -y --> up         y --> down


def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


# translated = translate(img, 100, 100)
# cv.imshow('Translated', translated)

# Rotation


def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(rotated, -45)
cv.imshow('Rotated Rotated', rotated_rotated)

# Resizing

# Flipping
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)

# cropping

#0- vertical
#1- horizontal
# -1 - both h and v

cv.waitKey(0)
