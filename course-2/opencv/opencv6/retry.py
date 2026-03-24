# This activity will guide students through
# accessing their computer’s camera and 
# performing real-time face detection using
# OpenCV’s pre-trained Haar Cascade classifier.
import cv2

# Load the Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start video capture from the webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break
    # Convert the frame to grayscale for face detection
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))
    for (x, y, w, h) in faces:
        #cv2.circle(img, center, radius, color, thickness=1, lineType=cv2.LINE_AA, shift=0)
        cv2.circle(frame, (x + w//2, y + h//2), radius=w//2, color=(255,127.5,0), thickness=2)
    # Display the resulting frame
    cv2.imshow('Face Detection - press Q to quit', frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()