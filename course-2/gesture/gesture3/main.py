# Build a complete, working gesture detection 
# system that uses a webcam to track hands in 
# real-time, identifies all finger positions, 
# and classifies gestures as Open, Closed Fist, or Partial.
import cv2
import mediapipe as mp
print(mp.__version__)
print(dir(mp))
print('solutions' in dir(mp))
print(mp.__file__)

# Initialize MediaPipe Hands
# mp.solutions -> collection of ready-made AI solutions (face detection, pose, hands, etc.)
# hands -> module used to detect and track hands
mp_hands = mp.solutions.hands

# 1. min_detection_confidence = 0.7. Minimum confidence required to detect a hand
# 0.5 -> easier detection but may increase false positives; 0.7 -> more accurate (range: 0 to 1).
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
# This loads the drawing utilities provided by MediaPipe.  It is used to draw landmarks and connections on the hand.
mp_draw = mp.solutions.drawing_utils

def detect_gesture(hand_landmarks):
    landmarks = hand_landmarks.landmark # hand_landmarks.landmark is a list containing 21 landmark objects.
    # x: horizontal position
    # y: vertical position
    # z: depth position
    tip_ids = [4, 8, 12, 16, 20]
    pip_ids = [2, 6, 10, 14, 18]
    extended = 0
    # If the difference is greater than 0.04, the thumb is considered open.
    if abs(landmarks[tip_ids[0]].x - landmarks[pip_ids[0]].x) > 0.04:
       extended += 1
    # Thumb moves sideways, not up and down like other fingers, so we check horizontal distance for thumb
    for i in range(1, 5):
        #Top of image = smaller y ---   Bottom = larger y
        if landmarks[tip_ids[i]].y < landmarks[pip_ids[i]].y:
           extended += 1
    if extended >= 4:
        return "Open"
    elif extended <= 1:
        return "Closed Fist"
    else:
        return "Partial"

# Start webcam
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
    
    # Detecting left hand and right hand landmarks
    # multi_hand_landmarks: 21 landmark points for each detected hand
    # multi_handedness: identifies whether each hand is Left or Right
    # results.multi_hand_landmarks: list of all detected hands
    if results.multi_handedness and results.multi_hand_landmarks:
        # idx mapping:
        # 0 -> first detected hand
        # 1 -> second detected hand
        for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
            # hand_label -> "Left" or "Right" for the detected hand
            hand_label = results.multi_handedness[idx].classification[0].label
            gesture = detect_gesture(hand_landmarks)
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Display the gesture and hand label on the frame
            # This part of the code marks the fingertips on the webcam frame and labels them wittheir MediaPipe landmark IDs.
    status_color = (0, 255, 0) if gesture in ["Open", "Closed Fist"] else (0, 165, 255)
    cv2.putText(frame, f"Gesture: {gesture}", (10, 30),
    cv2.FONT_HERSHEY_SIMPLEX, 1, status_color, 2)
    cv2.imshow("Hand Gesture Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
