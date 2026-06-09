import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

eye_cascade = cv2.CascadeClassifier(os.path.join(BASE_DIR, 'models/haarcascade_eye.xml'))
smile_cascade = cv2.CascadeClassifier(os.path.join(BASE_DIR, 'models/haarcascade_smile.xml'))
face_cascade = cv2.CascadeClassifier(os.path.join(BASE_DIR, 'models/haarcascade_frontalface_default.xml'))

def detect_blink(frame_gray, face):
    (x, y, w, h) = face
    roi_gray = frame_gray[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 4)
    return len(eyes) >= 2  # if 2 eyes detected → not blinking

def detect_smile(frame_gray, face):
    (x, y, w, h) = face
    roi_gray = frame_gray[y:y+h, x:x+w]
    smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 22)
    return len(smiles) > 0

def detect_head_movement(prev_nose, current_nose):
    if prev_nose is None:
        return False
    dx = abs(current_nose[0] - prev_nose[0])
    dy = abs(current_nose[1] - prev_nose[1])
    return dx > 15 or dy > 15  # threshold for movement