import cv2
import numpy as np
from scipy import ndimage

video = cv2.VideoCapture(0)

i = 0
kernel = np.ones((5, 5), np.uint8)
while True:

    ret, frame = video.read()
    if ret == False:
        break
    cv2.imshow("Color", frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if i == 20:
        bgGray = gray
    elif i > 20:
        dif = cv2.absdiff(gray, bgGray)
        cv2.imshow("Resta", dif)
        _, th = cv2.threshold(dif, 40, 255, cv2.THRESH_BINARY)
        # cnts, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # cv2.drawContours(frame, cnts, -1, (255, 0, 0), 5)
        cv2.imshow("Umbralisado", th)

        opening = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel)
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
        cv2.imshow("pre-Filtrado", closing)
        src = closing.copy()

        cv2.floodFill(src, None, (5, 5), (255, 0, 0))

        cv2.imshow("llenado", src)

    i = i + 1

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break
video.release()
