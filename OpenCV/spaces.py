import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos\park.jpg')
cv.imshow('Park', img)


# BGR to Grayscale
#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Grey image', gray)

# BGR TO HSV(Hue Saturation Value)
#hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#cv.imshow('HSV Image', hsv)

# BGR to LAB
#lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
#cv.imshow('LAB Image', lab)

# BGR to RGB
#rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
#cv.imshow('RGB', rgb)

# plt.imshow(rgb)
# plt.show()

# splitting into color channels
b, g, r = cv.split(img)

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b, g, r])
cv.imshow('Merged Image', merged)

cv.waitKey(0)
