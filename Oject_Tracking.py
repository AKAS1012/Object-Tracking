import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

img = np.zeros([512, 512, 3], np.uint8)
img = cv.line(img, (0, 0), (0, 0), (147, 0, 0), 10)

img = cv.circle(img, (70, 78), 67, (0, 0, 225), 1)

while cap.isOpened():
    ret, frame = cap.read()

    print(img.shape)
    print(frame)

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_green = np.array([80, 100, 100])
    upper_green = np.array([100, 255, 255])

    masks = cv.inRange(hsv, lower_green, upper_green)

    result = cv.bitwise_and(frame, frame, mask=masks)

    cv.imshow('frame', frame)
    cv.imshow('mask', masks)
    cv.imshow('result', result)

    key = cv.waitKey(1)
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()
