# Students will experiment with applying real-time 
# color filters and edge detection effects to a 
# sample image or webcam feed. They will toggle 
# between filters and edge detection techniques 
# using keyboard input and observe the effects instantly.
import cv2
import numpy as np
# Start webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Press 's' for Sobel Edge Detection,\nPress 'c' for Canny Edge Detection,\nPress 'r' for Red Tint,\nPress 'g' for Green Tint,\nPress"
      "'b' for Blue Tint,\nPress 'i' to Increase Red Tint,\nPress 'd' to Decrease Red Tint,\n" 
      "Press 'n' to Reset Filters,\nPress 'q' to Quit.")

# Initialize filter mode    
filter_mode = 0  # 0: None, 1: Color Filter, 2: Edge Detection
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break
    
    og_img = frame.copy()
    cv2.imshow('Original Image', og_img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s') or key == ord('S'):
        filter_mode = 2
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #dst = cv2.Sobel(src, ddepth, dx, dy[, ksize[, scale[, delta[, borderType]]]])
        sobelx = cv2.Sobel(grey, cv2.CV_64F, 1, 0, ksize=0)
        sobely = cv2.Sobel(grey, cv2.CV_64F, 0, 1, ksize=0)
        sobelxy = cv2.bitwise_or(sobelx.astype('uint8'), sobely.astype('uint8'))
        img = cv2.cvtColor(sobelxy, cv2.COLOR_GRAY2BGR)
        cv2.imshow('Sobel Edge Detection', img)
    elif key == ord('c') or key == ord('C'):
        filter_mode = 2
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(grey, 100, 200)
        img = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        cv2.imshow('Canny Edge Detection', img)
    elif key == ord('n') or key == ord('N'):
        cv2.imshow('original', og_img)
    elif key == ord('r') or key == ord('R'):
        filter_mode = 1
        frame[:, :, 1] = frame[:, :, 0] = 0
        cv2.imshow('Red Tint', frame)
    elif key == ord('i') or key == ord('I'):
        frame[:, :, 2] = cv2.add(frame[:, :, 2], 50)
        cv2.imshow('Red Tint', frame)
    elif key == ord('d') or key == ord('D'):
        frame[:, :, 2] = cv2.subtract(frame[:, :, 2], 50)
        cv2.imshow('Red Tint', frame)
    elif key == ord('g') or key == ord('G'):
        filter_mode = 1
        frame[:,:, 0] = frame[:, :, 2] = 0
        cv2.imshow('Green Tint', frame)
    elif key == ord('b') or key == ord('B'):
        filter_mode = 1
        frame[:, :, 1] = frame[:, :, 2] = 0
        cv2.imshow('Blue Tint', frame)
    elif key == ord('q') or key == ord('Q'):
        exit()
        cap.release()    
        cv2.destroyAllWindows()
    else:
        print("Invalid key. Please try again.")
    