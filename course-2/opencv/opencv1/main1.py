# In this activity, students will load an image, 
# convert it to grayscale, resize it to a standard 
# size (224x224), display the processed image, 
# and optionally save it based on key press.
import cv2
print(cv2.__version__)

# Read the image
img = cv2.imread("course-2/opencv/opencv1/monk.png")
if img is None:
    print("Could Not Read Image")
else:
    print("Image loaded successfully")
    cv2.namedWindow("Monk Image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Monk Image", 600, 400)
    # Convert to Grayscale
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Monk Image", grey_img)
    key = cv2.waitKey(0)
    if key == ord("s"):
        cv2.imwrite("course-2/opencv/opencv1/monk_gray.png", grey_img)
        print("Image saved as monk_gray.png.")
    cv2.destroyAllWindows()