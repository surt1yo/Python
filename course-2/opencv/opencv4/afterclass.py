# Build on the concepts learned in class by 
# developing an application that allows users 
# to upload images, apply edge detection techniques 
# (Sobel, Canny, Laplacian), and test different 
# filtering methods (Gaussian, Median) interactively.
import cv2
from matplotlib.pylab import choice
import matplotlib.pyplot as plt
import numpy as np

# Read the image
image = cv2.imread("course-2/opencv/opencv1/monk.png")
if image is None:
    print("Error: Could not load image.")
    exit()

# Convert to Grayscale
grey_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
plt.imshow(grey_image, cmap="gray")
print("1. Sobel detection\n2. Canny detection\n"
"3. Laplacian detection\n4. Gaussian Blue\n5. Median Filtering\n6. Exit")
choice = input("Select an option for edge detection (1-6):")

while True:                                                                                  
    if choice == "1":
        print("Sobel Edge Detection Starting:")
        sobelx = cv2.Sobel(grey_image, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(grey_image, cv2.CV_64F, 0, 1, ksize=3)
        sobel_combo = cv2.bitwise_or(sobelx.astype(np.uint8), sobely.astype(np.uint8), None, None)
        plt.imshow(sobel_combo, cmap='gray')
        plt.title("Sobel Edge Detection")
        plt.show()

    elif choice == "2":
        print("Canny Edge Detection Starting:")
        print("Adjust thresholds for Canny (default: 100 and 200)")
        low_thresh = int(input("Enter low threshold: "))
        high_thresh = int(input("Enter high threshold: "))
        edges = cv2.Canny(grey_image, low_thresh, high_thresh)
        plt.imshow(edges, cmap='gray')
        plt.title("Canny Edge Detection")
        plt.show()

    elif choice == "3":
        print("Laplacian Edge Detection Starting:")
        laplacian = cv2.Laplacian(grey_image, cv2.CV_64F)
        plt.imshow(laplacian.astype(np.uint8), cmap='gray')
        plt.title("Laplacian Edge Detection")
        plt.show()

    elif choice == "4":
        print("Gaussian Blur Starting:")
        gaussian_blur = cv2.GaussianBlur(grey_image,(5, 5), 1.4) 
        plt.imshow(gaussian_blur, cmap='gray')
        plt.title("Gaussian Blur")
        plt.show()

    elif choice == "5":
        print("Median Filtering Starting:")
        median_blur = cv2.medianBlur(grey_image, 5)
        plt.imshow(median_blur, cmap='gray')
        plt.title("Median Filtering")
        plt.show()

    elif choice == "6":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option (1-6).")
        