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
    #cv2.CascadeClassifier.detectMultiScale(image, scaleFactor(), minNeighbors[, flags[, minSize[, maxSize]]]]]
    faces = face_cascade.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))

    # Draw rectangles around detected faces
    for (x, y, w , h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)

    # Display the resulting frame
    cv2.imshow('Face Detection- press Q to quit', frame)
    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
    
