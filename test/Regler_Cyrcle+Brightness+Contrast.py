import cv2

face_cascade = cv2.CascadeClassifier(
        f'{cv2.data.haarcascades}haarcascade_frontalface_default.xml')

def funcBrightContrast(bright=0):
    bright = cv2.getTrackbarPos('bright', 'Life2Coding')
    contrast = cv2.getTrackbarPos('contrast', 'Life2Coding')

    effect = apply_brightness_contrast(red_channel,bright,contrast)
    cv2.imshow('Effect', effect)

def apply_brightness_contrast(input_img, brightness = 255, contrast = 127):
    brightness = map(brightness, 0, 510, -255, 255)
    contrast = map(contrast, 0, 254, -127, 127)

    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + brightness
        alpha_b = (highlight - shadow)/255
        gamma_b = shadow

        buf = cv2.addWeighted(input_img, alpha_b, input_img, 0, gamma_b)
    else:
        buf = input_img.copy()

    if contrast != 0:
        f = float(131 * (contrast + 127)) / (127 * (131 - contrast))
        alpha_c = f
        gamma_c = 127*(1-f)

        buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)

    cv2.putText(buf,'B:{},C:{}'.format(brightness,contrast),(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    return buf

def map(x, in_min, in_max, out_min, out_max):
    return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)

if __name__ == '__main__':
    camera = cv2.VideoCapture(0)
    while (cv2.waitKey(1) == -1):
        success, frame = camera.read()
        if success:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(
                gray, 1.3, 5, minSize=(120, 120))
            for (x, y, w, h) in faces:
                # cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                roi_gray = gray[y:y + h, x:x + w]
                frame_cpy = frame.copy()
                cv2.circle(frame, (int(x + w / 2), int(y + h / 2)), int(h / 2), (0, 0, 255), cv2.FILLED, 2)
                alpha = 0.4
                frame_overlay = cv2.addWeighted(frame, alpha, frame_cpy, 1 - alpha, gamma=0)

                # for (ex, ey, ew, eh) in eyes:
                #     cv2.rectangle(frame, (x+ex, y+ey),
                #                   (x+ex+ew, y+ey+eh), (0, 255, 0), 2)
                cv2.imshow("overlay result", frame_overlay)

    #cv2.circle(frame, (int(x + w / 2), int(y + h / 2)), int(h / 2), (0, 0, 255), cv2.FILLED, 2)
                original = cv2.imread("overlay result", 1)
                #original = cv2.resize(original, None, fx=0.1, fy=0.1)

                #red_channel = frame_overlay()

                #red_channel[:, :, 1] = 0
                #red_channel[:, :, 0] = 0

                #cv2.namedWindow('Life2Coding',1)

                bright = 255
                contrast = 127

    #Brightness value range -255 to 255
    #Contrast value range -127 to 127

                cv2.createTrackbar('bright', 'Life2Coding', bright, 2*255, funcBrightContrast)
                cv2.createTrackbar('contrast', 'Life2Coding', contrast, 2*127, funcBrightContrast)
                funcBrightContrast(0)
                cv2.imshow('Life2Coding', original)


cv2.waitKey(0)

