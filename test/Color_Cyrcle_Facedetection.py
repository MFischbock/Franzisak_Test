import cv2

face_cascade = cv2.CascadeClassifier(
    f'{cv2.data.haarcascades}haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(
    f'{cv2.data.haarcascades}haarcascade_eye.xml')
camera = cv2.VideoCapture(0)
while (cv2.waitKey(1) == -1):
    success, frame = camera.read()
    if success:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray, 1.3, 5, minSize=(120, 120))
        for (x, y, w, h) in faces:
            #cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            frame_cpy = frame.copy()
            cv2.circle(frame, (int(x+w/2), int(y+h/2)), int(h/2), (0, 0, 255),cv2.FILLED, 2)
            alpha = 0.4
            frame_overlay = cv2.addWeighted(frame, alpha, frame_cpy, 1 - alpha, gamma=0)
            eyes = eye_cascade.detectMultiScale(
                roi_gray, 1.11, 5, minSize=(40, 40))
            # for (ex, ey, ew, eh) in eyes:
            #     cv2.rectangle(frame, (x+ex, y+ey),
            #                   (x+ex+ew, y+ey+eh), (0, 255, 0), 2)
        cv2.imshow("overlay result", frame_overlay)
