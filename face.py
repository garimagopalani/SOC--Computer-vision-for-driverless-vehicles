import cv2 as cv
import numpy as np

img = cv.imread('D:/IITB/Design/face.jpg')
cv.imshow('Face', img)

gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

gray_img= cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
cv.imshow('gray 3 channel', gray_img)

x,y, width, height= 180, 250, 250, 350
roi= gray[y:y+height, x:x+width] #region of interest, only make this part blur
#cv.imshow('ROI', roi)

blur= cv.GaussianBlur(roi, (17,17),0)
#cv.imshow('Blur', blur)

gray[y:y+height, x:x+width]= blur
#cv.imshow('Modified Image', gray)

full_blur= cv.GaussianBlur(gray, (3,3),0)
cv.imshow('Blur', full_blur)

edges1=cv.Canny(full_blur, 100, 120)
cv.imshow('Edges1', edges1)

edges2=cv.Canny(full_blur, 80, 100)
cv.imshow('Edges2', edges2)


result=np.copy(gray_img)
result[edges2!=0]= [255,0,0]
result[edges1!=0]= [0,0,255]
cv.imshow('Result', result)

cv.waitKey(0)