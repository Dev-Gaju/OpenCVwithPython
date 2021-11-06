# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 03:37:26 2021

@author: gazur
"""

import cv2
import mediapipe as mp
import time

cap= cv2.VideoCapture(0)



print(cv2.__version__)

#want point number 5 from hand

mpHand= mp.solutions.hands
hands= mpHand.Hands() #have default parameter  #staticlavel= false mean faster 
mpDraw= mp.solutions.drawing_utils

#time set
pTime=0
cTime= 0

while True:
    success, img= cap.read()
    imgRGB= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results =hands.process(imgRGB)
    #extract multiple hands
#     print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:  #each hands
            #check the id and landmarks
            for id, lm in enumerate(handLms.landmark):
                
                #0 is bottom middle
                #land mark have x,y,z 
                #location in pixel given ratio of image
                #print(id, landmark)
                h,w,c=img.shape  #height, width, channel
                cx, cy=int(lm.x*w), int(lm.y*h) 
                #position of center 
                #print(id, cx, xy)
                if id==0:  #first landmark
                    cv2.circle(img, (cx,cy), 10,(255,0,255), cv2.FILLED)     
            mpDraw.draw_landmarks(img, handLms, mpHand.HAND_CONNECTIONS)  # HAND_CONNECTIONS draw connection    
            #got hand connection with 21 landmarks
    
    cTime= time.time()
    fps=1/(cTime-pTime)
    pTime= cTime
    
    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)   #tesxt on video
    cv2.imshow("Image", img)
    cv2.waitKey(1)