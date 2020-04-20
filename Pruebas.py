import cv2
import numpy as np

cap = cv2.VideoCapture(0)
_, prev = cap.read()
prevG = cv2.cvtColor(prev, cv2.COLOR_RGB2GRAY)
kernel = np.ones((5, 5), np.uint8)
while True:
    _, next = cap.read()
    nextG = cv2.cvtColor(next, cv2.COLOR_RGB2GRAY)
    flow = np.array(
        abs(np.array(nextG, np.float32) - np.array(prevG, np.float32)), np.uint8
    )
    cv2.imshow("Diferencia", flow)
    rang = cv2.inRange(flow, 20, 255)
    # cv2.imshow("rango", rang)
    opening = cv2.morphologyEx(rang, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("pre-Filtrado", closing)

    prev = next
    cv2.imshow("Siguiente", next)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
