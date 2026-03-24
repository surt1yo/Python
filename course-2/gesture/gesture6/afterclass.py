# In this assignment, you will enhance your 
# gesture-controlled photo app by experimenting 
# with different hand gestures to capture images
# and apply dynamic filters (grayscale, sepia, negative, blur). 
# You will implement the logic to switch between different 
# filters based on hand gestures, such as thumb touching 
# the index finger for photo capture and thumb 
# touching any other finger for changing filters.
import cv2, time, mediapipe as mp, numpy as np

# Mediapipe Setup
mp_hands  = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Tips of fingers
tips = mp_hands.HandLandmark
ids = {
    "thumb": tips.THUMB_TIP,
    "index": tips.INDEX_FINGER_TIP,
    "middle": tips.MIDDLE_FINGER_TIP,
    "ring": tips.RING_FINGER_TIP,
    "pinky": tips.PINKY_TIP
}

# Pairs of fingers for gesture recognition
pairs = {"middle":("SEPIA","NEGATIVE"), 
         "ring":("BLUR","GLITCH"),
         "pinky":("EDGE","CARTOON")}
st = {k:0 for k in pairs}; cur = "SEPIA"
DEB, CAP, TT, TP = 0.6, 1.2, 30, 20
la = lc = 0; pinch_on = False
MAIN, POP = "Gesture-Controlled Photo App", "Captured (ESC / Close to resume)"
paused = False; freeze = None
SEPIA_M = np.array([[0.272,0.534,0.131],
                    [0.349,0.686,0.168],
                    [0.393,0.769,0.189]])

# Function to apply filters based on gesture
def apply(img, t):
    if t == "SEPIA": 
        return np.clip(cv2.transform(img, SEPIA_M), 0, 255).astype(np.uint8)
    elif t == "NEGATIVE": 
        return cv2.bitwise_not(img)
    elif t == "BLUR": 
        return cv2.GaussianBlur(img, (15, 15), 0)
    elif t == "GLITCH":
        h,w = img.shape[:2]; r,g,b = img[:,:,2], img[:,:,1], img[:,:,0]
        return cv2.merge([np.roll(b, -int(0.02*w), 1), g, np.roll(r, int(0.04*w), 1)])
    elif t == "EDGE":
        return cv2.Canny(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 80, 160)
    elif t == "CARTOON":
        g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        e = cv2.adaptiveThreshold(cv2.medianBlur(g, 7), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)
        c = cv2.bilateralFilter(img, 9, 75, 75)
        return cv2.bitwise_and(c, c, mask=e)
    return img

# Capturing video from webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img)
    now = time.time(); capture = False
    if results.multi_hand_landmarks:
        hand = results.multi_hand_landmarks[0]
        mp_drawing.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
        lm = hand.landmark
        tips = {k:(int(lm[v].x*w), int(lm[v].y*h)) for k,v in ids.items()}
        tx,ty = tips["thumb"]; ix,iy = tips["index"]
        pinch = abs(tx-ix) < TP and abs(ty-iy) < TP
        if pinch and not pinch_on and now-lc > CAP: pinch_on = True; capture = True; lc = now
        if not pinch and pinch_on: pinch_on = False
        if not pinch:
            t = next((k for k in pairs if abs(tx-tips[k][0]) < TT and abs(ty-tips[k][1]) < TT), None)
            if t and now-la > DEB: cur = pairs[t][st[t]]; st[t] ^= 1; la = now; print("Filter:", cur)
                 
    out = apply(img, cur)
            
    if cur == "EDGE":
        out = cv2.cvtColor(out, cv2.COLOR_GRAY2BGR)
    if capture:
        name = f"picture_{int(now)}.jpg"; cv2.imwrite(name, out); print("Saved:", name)
        paused, freeze = True, out.copy(); cv2.imshow(POP, freeze)
    cv2.imshow(MAIN, out)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows() 
hands.close()
        