import cv2
from cvzone.HandTrackingModule import HandDetector
import time
cap=cv2.VideoCapture(0)
handdetector=HandDetector(maxHands=1) #imported hand detection from cvzone
offset=20
folder="images/A"
while True:
    success,img=cap.read()
    hands,img=handdetector.findHands(img) #read hand

    if hands:
        hand=hands[0]
        x,y,w,h=hand['bbox']
        imgcrop=img[y-offset:y+h+offset,x-offset:x+h+offset]
        cv2.imshow("cropimage",imgcrop)

    cv2.putText(img, "press q to quit", (240, 450),cv2.FONT_HERSHEY_DUPLEX, 1, (0,250, 0), 2)
    cv2.imshow("sign detection",img)
    key=cv2.waitKey(1)
    if key==ord("s"):
        cv2.imwrite(f'{folder}/image_{time.time()}.jpg',imgcrop)


