import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone
import math
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)


detector = HandDetector(detectionCon=0.8, maxHands=1)



x = [450, 395, 320, 270, 225, 215]
y = [20, 25, 30, 35, 40, 45]

# x = [0.22,0.2,0.18,0.14,0.11,0.9]
# y = [20,25,30,35,40,45]


coff = np.polyfit(x,y,2)
A,B,C = coff
print(A,B,C)


while True:
  success, img = cap.read()
  hands = detector.findHands(img, draw = False)

  if hands:
    lmlist = hands[0]['lmList']
    x,y,w,h = hands[0]['bbox']
    x1, y1 = lmlist[5]
    x2, y2 = lmlist[17]

    distance = int(math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2))
    distanceCM = A*distance**2 + B*distance + C
    
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 3)
    cvzone.putTextRect(img, f'{int(distanceCM)} cm', (x+5, y-10))

  cv2.imshow("Image", img)
  cv2.waitKey(1)


