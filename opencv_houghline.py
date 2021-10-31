import time
import cv2
import numpy as np
import math

theta=0
minLineLength = 5
maxLineGap = 10
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 85, 85)

    lines = cv2.HoughLinesP(edges,1,np.pi/180,10,minLineLength,maxLineGap)
    if(lines is not None):
        for x in range(0, len(lines)):
            for x1,y1,x2,y2 in lines[x]:
                cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),2)
                theta=theta+math.atan2((y2-y1),(x2-x1))

    threshold=6
    if(theta>threshold):
        print("left")
    if(theta<-threshold):
        print("right")
    if(abs(theta)<threshold):
        print ("straight")

    theta=0
    cv2.imshow("Frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
