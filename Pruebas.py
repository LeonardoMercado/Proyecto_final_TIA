import cv2
import numpy as np

video = cv2.VideoCapture(0)

i = 0

while True:

    ret, frame = video.read()
    if ret == False:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if i == 20:
        bgGray = gray
    elif i > 20:
        dif = cv2.absdiff(gray, bgGray)
        cv2.imshow("Resta", dif)
        _, th = cv2.threshold(dif, 40, 255, cv2.THRESH_BINARY)
        cnts, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # cv2.drawContours(frame, cnts, -1, (255, 0, 0), 5)
        # cv2.imshow("Resta", th)
    # cv2.imshow("HolaMundo", gray)

    i = i + 1

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break
video.release()
