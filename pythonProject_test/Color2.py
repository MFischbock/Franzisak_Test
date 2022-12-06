import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    if ret:

        # hsv is better to recognize color, convert the BGR frame to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # in hsv red color located in two region. Create the mask for red color
        # mask the red color and get an grayscale output where red is white
        # everything else are black
        mask1 = cv2.inRange(hsv, (0,50,20), (5,255,255))
        mask2 = cv2.inRange(hsv, (175,50,20), (180,255,255))
        mask = cv2.bitwise_or(mask1, mask2)

        # get the index of the white areas and make them orange in the main frame
        for i in zip(*np.where(mask == 255)):
                frame[i[0], i[1], 0] = 0
                frame[i[0], i[1], 1] = 165
                frame[i[0], i[1], 2] = 255

        # play the new video
        cv2.imshow("res",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cv2.destroyAllWindows()