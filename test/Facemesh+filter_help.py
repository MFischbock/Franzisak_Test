import cv2
import mediapipe as mp
import time
import numpy as np
import math
from typing import Tuple

cap = cv2.VideoCapture(0)
pTime = 0

def getLandmarks(img):
mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5, max_num_faces=1)
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1, color=RED_COLOR)
RED_COLOR = (0, 0, 255)
mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh

#die äußeren landmarks nehmen und als Kontur nehmen
selected_keypoint_indices = [127, 93, 58, 136, 150, 149, 176, 148, 152, 377, 400, 378, 379, 365, 288, 323, 356,
                                 70, 63, 105, 66, 55,
                                 285, 296, 334, 293, 300, 168, 6, 195, 4, 64, 60, 94, 290, 439, 33, 160, 158, 173,
                                 153, 144, 398, 385,
                                 387, 466, 373, 380, 61, 40, 39, 0, 269, 270, 291, 321, 405, 17, 181, 91, 78, 81,
                                 13, 311, 306, 402, 14,
                                 178, 162, 54, 67, 10, 297, 284, 389]

height, width = img.shape[:-1]


while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACEMESH_CONTOURS,
                                  drawSpec,drawSpec)
            for id,lm in enumerate(faceLms.landmark):
                #print(lm)
                ih, iw, ic = img.shape
                x,y = int(lm.x*iw), int(lm.y*ih)
                print(id,x,y)
    #convexhull = cv2.convexhull(cvt)
    #mask = np.zero((height, widht), np.uint8)
    #cv2.fillConvexPoly(mask, convexhull, 255)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)