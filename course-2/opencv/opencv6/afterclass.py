# In this project, students will extend real-time 
# face detection by adding emotion recognition. 
# Using the OpenCV face detection technique,
# students will integrate a pre-trained emotion 
# recognition model to classify facial expressions.
import cv2
from deepface import DeepFace

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

frame_count = 0
emotion_cache = {}  # store last detected emotion for each face

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))

    frame_count += 1
    for i, (x, y, w, h) in enumerate(faces):
        roi_color = frame[y:y+h, x:x+w]

        # Only analyze every 5 frames to reduce lag
        if frame_count % 5 == 0:
            try:
                predictions = DeepFace.analyze(roi_color, actions=['emotion'], enforce_detection=False)
                emotion_cache[i] = predictions[0]['dominant_emotion']
            except:
                emotion_cache[i] = "Unknown"

        emotion = emotion_cache.get(i, "Unknown")

        # Draw circle around face
        cv2.circle(frame, (x + w//2, y + h//2), radius=w//2, color=(255,127,0), thickness=2)
        # Put emotion text
        cv2.putText(frame, emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)

    cv2.imshow('Real-Time Emotion Recognition - Q to Quit', frame)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()