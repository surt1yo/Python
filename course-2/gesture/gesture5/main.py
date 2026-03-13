# Students will build a gesture-controlled scroll 
# system that detects hand gestures in real-time 
# and controls the system’s scrolling behavior 
# based on whether the hand is open or closed.
import cv2, mediapipe as mp, time, pyautogui

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Function to detect gesture based on hand landmarks
def detect_gesture(landmarks, handedness):
    tips = [mp_hands.HandLandmark.INDEX_FINGER_TIP,
                mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
                mp_hands.HandLandmark.RING_FINGER_TIP,
                mp_hands.HandLandmark.PINKY_TIP]
    fingers = []
    # Check fingers (except thumb)
    for tip in tips:
        if landmarks.landmark[tip].y < landmarks.landmark[tip - 2].y:
            fingers.append(1)
        else:     
             fingers.append(0)
    # Thumb tip
    thumb_tip=landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_ip=landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
    if (handedness == "Right" and thumb_tip.x > thumb_ip.x) or (handedness == "Left" and thumb_tip.x < thumb_ip.x):
        fingers.append(1) 
    if sum(fingers)==5:
        return "scroll_up"
    elif sum(fingers)==0:
        return "scroll_down"
    else:
        return "None"
    print(sum(fingers))


    
# Activating the webcam
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

    # Dimensions of the frame
    h, w, _ = frame.shape

    # Convert the image to RGB as MediaPipe uses RGB format
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the image and find hands
    results = hands.process(img_rgb)
    gesture = "Unknown"
    # Detecting Left and Right hand landmarks
    if results.multi_handedness and results.multi_hand_landmarks:
        for hand, handedness_info in zip(results.multi_hand_landmarks, results.multi_handedness):
            handedness = handedness_info.classification[0].label
            mp_drawing.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
            gesture = detect_gesture(hand, handedness)
            cv2.putText(frame, f"Hand: {handedness} | Gesture: {gesture}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow("Hand Gesture Control", frame)
    if gesture == "scroll_up":
        pyautogui.scroll(200) 
    elif gesture == "scroll_down":
        pyautogui.scroll(-200)  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
            