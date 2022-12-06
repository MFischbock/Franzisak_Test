import cv2
import numpy as np
import mediapipe as mp
from facial_landmarks import FaceLandmarks
# Load face landmarks
fl = FaceLandmarks()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame_copy = frame.copy()
    height, widht, _ = frame.shape
    #1. Face landmarks detection = Zone vom Gesicht bekommen
    landmarks = fl.get_facial_landmarks(frame)

    #for i in range(0,468):
        #pt = landmarks[i]
        # landmarks in Punkten dargestellt pt(0) = höhe, pt(1) = breite, 5 = Durchmesser, (0,0,255) = Farbe rot
        #cv2.circle(frame, (pt[0], pt[1]), 5, (0,0,255))
    # wir wollen aber nicht alle landmarks sondern nur die, die das Gesicht abgrenzen
    convexhull = cv2.convexhull(landmarks)
    #cv2.polylines(frame,[convexhull], True, (0, 0, 255), 2)

    # 2. Maske erstellen
    mask = np.zero((height, widht), np.uint8)
    #cv2.polylines(mask,[convexhull], True, 255, 2)
    cv2.fillConvexPoly(mask, convexhull, 255)

    # extract the face
    frame_copy = cv2.blur(frame_copy, (5, 5))
    face.extracted = cv2.bitwise_and(frame_copy, frame_copy, mask=mask)
    # 3. Face Blurrying bzw. change color
    blurred_face = cv2.GaussianBlur(face_extracted, (5, 5), 0)

    # extract background
    background_mask = cv2.bitwise_not(mask)
    background = cv2.bitwise_and(frame, frame, mask=background_mask)

    # Final result
    result = cv2.add(background, blurred_face)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("background", background)
    cv.2.imshow("Face extracted", blurred_face)
    cv2.imshow("Result", result)

    key = cv2.waitkey(30)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()