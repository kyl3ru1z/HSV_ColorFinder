import cv2
import numpy as np

def empty(a):
    pass


cv2.namedWindow("Track Bars")
cv2.resizeWindow("Tracked Bars", 640, 480)
cv2.createTrackbar("Hue Min", "Track Bars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "Track Bars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "Track Bars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "Track Bars", 255, 255, empty)
cv2.createTrackbar("Value Min", "Track Bars", 0, 255, empty)
cv2.createTrackbar("Value Max", "Track Bars", 255, 255, empty)

# second property fixes a bug
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# Frame Width
cap.set(3, 640)
# Frame Height
cap.set(4, 480)
# adjusting brightness
cap.set(10, 140)

while True:
    success, video = cap.read()

    videoFlip = cv2.flip(video, 1)
    videoHSV = cv2.cvtColor(videoFlip, cv2.COLOR_BGR2HSV)

    hueMin = cv2.getTrackbarPos("Hue Min", "Track Bars")
    hueMax = cv2.getTrackbarPos("Hue Max", "Track Bars")
    satMin = cv2.getTrackbarPos("Sat Min", "Track Bars")
    satMax = cv2.getTrackbarPos("Sat Max", "Track Bars")
    valMin = cv2.getTrackbarPos("Value Min", "Track Bars")
    valMax = cv2.getTrackbarPos("Value Max", "Track Bars")

    lower = np.array([hueMin, satMin, valMin])
    upper = np.array([hueMax, satMax, valMax])

    mask = cv2.inRange(videoHSV, lower, upper)

    cv2.imshow("HSV", videoHSV)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
