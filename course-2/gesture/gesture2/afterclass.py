# In this assignment, you will continue 
# experimenting with the image processing 
# techniques covered in the lesson, 
# focusing on applying color filters and 
# performing edge detection on images. 
# You will dynamically toggle between filters
# and edge detection methods using keyboard 
# input and observe the effects on real-time image processing.
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("""
Controls
s = Sobel Edge Detection
c = Canny Edge Detection
l = Laplacian Edge Detection
r = Red Tint
g = Green Tint
b = Blue Tint
i = Increase Red
d = Decrease Red
y = Grayscale
u = Blur
n = Reset
q = Quit
""")

mode = "normal"
red_boost = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    img = frame.copy()

    if mode == "red":
        img[:,:,1] = 0
        img[:,:,0] = 0
        img[:,:,2] = cv2.add(img[:,:,2], red_boost)

    elif mode == "green":
        img[:,:,0] = 0
        img[:,:,2] = 0

    elif mode == "blue":
        img[:,:,1] = 0
        img[:,:,2] = 0

    elif mode == "gray":
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    elif mode == "blur":
        img = cv2.GaussianBlur(img,(15,15),0)

    elif mode == "sobel":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        sobelx = cv2.Sobel(gray, cv2.CV_64F,1,0,ksize=3)
        sobely = cv2.Sobel(gray, cv2.CV_64F,0,1,ksize=3)
        sobel = cv2.magnitude(sobelx,sobely)
        sobel = np.uint8(np.absolute(sobel))
        img = cv2.cvtColor(sobel, cv2.COLOR_GRAY2BGR)

    elif mode == "canny":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray,100,200)
        img = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    elif mode == "laplacian":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        lap = cv2.Laplacian(gray,cv2.CV_64F)
        lap = np.uint8(np.absolute(lap))
        img = cv2.cvtColor(lap, cv2.COLOR_GRAY2BGR)

    cv2.imshow("Image Processing Lab", img)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        mode = "sobel"
    elif key == ord('c'):
        mode = "canny"
    elif key == ord('l'):
        mode = "laplacian"
    elif key == ord('r'):
        mode = "red"
    elif key == ord('g'):
        mode = "green"
    elif key == ord('b'):
        mode = "blue"
    elif key == ord('y'):
        mode = "gray"
    elif key == ord('u'):
        mode = "blur"
    elif key == ord('i'):
        red_boost = min(255, red_boost + 20)
    elif key == ord('d'):
        red_boost = max(0, red_boost - 20)
    elif key == ord('n'):
        mode = "normal"
        red_boost = 0
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()