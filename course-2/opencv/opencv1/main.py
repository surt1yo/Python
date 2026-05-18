# In this activity, students will learn how to load an 
# image using OpenCV, display it in a resizable window, 
# and adjust the window size. They will also explore 
# the properties of an image such as dimensions and channels.
import cv2
print(cv2.__version__)

# Reading an image
img = cv2.imread('course-2/opencv/opencv1/monk.png')
if img is None:
    print("Could not read the image.")
else:
    print("Image loaded successfully.")
    cv2.namedWindow('Monk Image', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Monk Image', 600, 400)
    cv2.imshow('Monk Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()