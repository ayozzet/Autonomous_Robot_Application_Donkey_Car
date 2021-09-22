import cv2

cap = cv2.VideoCapture(0) #common source = 0

while (True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.imshow("Original", frame)
    cv2.imshow("Grayscale", gray)
    cv2.imshow("RGB", rgb)
    cv2.imshow("HSV", hsv)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
