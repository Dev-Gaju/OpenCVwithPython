import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#color Space
#RBG, grayscale, HSV, LAB

#convert BGR to Grayscale

img = cv.imread("Photos/cat2.jpg")
cv.imshow("main Image", img)

plt.imshow(Photos/cat2.jpg")
plt.show()


grayScale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("GRAYsCALE  Image", grayScale)


#BGR TO HSV
#if define how human think and describe color

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV Image', hsv)

#BGR to LAB

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('Lab Image', lab)




cv.waitKey(0)