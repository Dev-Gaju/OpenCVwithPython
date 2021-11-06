import cv2
import mediapipe as mp
import time
import numpy as np
import os
import Hand_Detector_Module as hm

folder_path = "header files"
myList = os.listdir(folder_path)
print(myList)
overLaylist = []  # store image here

# import all the eader
for impath in myList:
    image = cv2.imread(f'{folder_path}/{impath}')
    overLaylist.append(image)

print(len(overLaylist))

header = overLaylist[0]
##########
drawColor=(255, 0, 255)
brushThicness=15
eraserThicness=50
imgCanvas= np.zeros((720,1280,3), np.uint8)

###########
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, 1280)
cap.set(4, 720)

detector = hm.HandDetector()
xp=0
yp=0
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  # flip horizonataly

    # 1. find landmarks
    img = detector.FindHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:

        # print(lmList)
        # tip of index or middle finger
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        # 2. ckeck finger write
        fingers = detector.Fingerup()
        # print(fingers)

        # 3. two finger up select mode
        if fingers[1] and fingers[2]:
            xp,yp= 0, 0   #come to black and purple in two picture

            # print("selection Mode")
            #checking for the click
            if y1 <99 :
                if 250<x1<450:
                    header=overLaylist[0]
                    drawColor=(0,255,0)
                elif 550<x1<950:
                    header=overLaylist[1]
                    drawColor=(0, 0, 255)
                elif 750<x1<1150:
                    header=overLaylist[2]
                    drawColor=(0, 0, 0)
            cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv2.FILLED)



        # 4 drawing mode if index up
        if fingers[1] and fingers[2] == False:
            cv2.circle(img, (x1,y1),15,  drawColor, cv2.FILLED)
            # print("Drawing Mode")
            if xp==0 and yp==0:
                xp, yp = x1, y1


            if drawColor == (0, 0, 0):
                cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThicness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThicness)
            else:
                cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThicness)
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThicness)



            #here jnow previous point and current point


            xp, yp = x1, y1  #previous point

    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)

    # settings the header image
    img[0:80, 0:1084] = header

    cv2.imshow('Image', img)
    cv2.imshow("image canvas", imgCanvas)
    cv2.imshow("inverse Image", imgInv)
    cv2.waitKey(1)
