import cv2 as cv

img = cv.imread('Photos\park.jpg')
cv.imshow('Park', img)

# converting to greyscale
#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Park-Greyscale', gray)

# blurring the image
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('Park-blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# dilate image using a structuring element
dilated = cv.dilate(canny, (3, 3), iterations=1)
cv.imshow('Dilated', dilated)

# eroding
eroded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow('Eroded', eroded)

# resizing
resized = cv.resize(img, (500, 500), interpolation = cv.IN )
cv.imshow('Resized', resized)

# cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
