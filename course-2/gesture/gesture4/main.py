# Students will build a real-time gesture control 
# system that adjusts the system volume and screen 
# brightness using hand gestures. By calculating 
# the distance between the thumb and index finger, 
# students will manipulate the volume and brightness 
# on their computer in real-time.
import cv2
import numpy as np
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, max_tracking_confidence=0.7)
