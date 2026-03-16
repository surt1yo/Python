# In this assignment, you will build a 
# real-time gesture control system that
# allows you to scroll up and down using
# hand gestures. Using MediaPipe for hand 
# tracking, PyAutoGUI for controlling scrolling,
# and OpenCV for real-time image processing,
# you will create an interactive gesture-based 
# controller that tracks your hand movements and 
# scrolls based on specific gestures 
# (open palm for scroll up, closed fist for scroll down).
import cv2
import mediapipe as mp
import pyautogui

# Mediapipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils

# Start webcam
cap = cv2.VideoCapture(0)

# Finger tip indexes
tips = [4, 8, 12, 16, 20]

def count_fingers(hand_landmarks):
    fingers = []

    # Thumb
    if hand_landmarks.landmark[tips[0]].x > hand_landmarks.landmark[tips[0] - 1].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers
    for i in range(1,5):
        if hand_landmarks.landmark[tips[i]].y < hand_landmarks.landmark[tips[i] - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return sum(fingers)

while True:

    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            finger_count = count_fingers(hand_landmarks)

            # Open palm → scroll up
            if finger_count >= 4:
                cv2.putText(frame, "SCROLL UP", (10,50),
                            cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)
                pyautogui.scroll(50)

            # Closed fist → scroll down
            elif finger_count == 0:
                cv2.putText(frame, "SCROLL DOWN", (10,50),
                            cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
                pyautogui.scroll(-50)

    cv2.imshow("Gesture Scroll Control", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()