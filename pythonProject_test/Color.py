import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    if ret:
        for i in zip(*np.where(frame == [0,255, 255])):
            frame[i[0], i[1], 0] = 0
            frame[i[0], i[1], 1] = 0
            frame[i[0], i[1], 2] = 0
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cv2.destroyAllWindows()