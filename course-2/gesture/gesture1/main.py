# Students will implement real-time 
# face tracking and counting using 
# their webcam. They will detect faces, 
# count the number of people in the frame, 
# and display the count dynamically.
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
    faces = face_cascade.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=5)
    # Draw rectangles around detected faces
    for (x, y, w , h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)

    # Count the number of faces detected
    face_count = len(faces)

    # Display the count on the frame
    cv2.putText(frame, f'Count: {face_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    # Increase brightness using convertScaleAbs
    bright_frame = cv2.convertScaleAbs(frame, alpha=1, beta=50)

    cv2.imshow("Video Brightness Control", bright_frame)
    
    # Display the resulting frame
    cv2.imshow('Face Detection- press Q to quit', frame)
    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xff == ord('q') or cv2.waitKey(1) & 0xff == ord('Q'):
        break
# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()