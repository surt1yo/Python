# In this project, you will apply fundamental 
# image manipulation techniques, including rotation, 
# cropping, and brightness adjustments, using OpenCV. 
# This project will deepen their understanding of how 
# these operations work and how they affect images 
# in the context of computer vision and AI applications.
import cv2
import numpy as np

# Read the image
image = cv2.imread("course-2/opencv/opencv1/monk.png")
image_org=image.copy()
if image is None:
    print("Error: Could not load image.")
    exit()
# Rotate the image by 45 degrees
(h, w) = image.shape[:2]
center = (w // 2, h // 2)

M  = cv2.getRotationMatrix2D(center, 45, 1.0)

# Brightness Adjustment
bright = cv2.convertScaleAbs(image_org, alpha=1, beta=50)

# Apply the rotation to the image
rotation = cv2.warpAffine(image, M, (w, h))

# Crop the image 
cropped = rotation[100:400, 150:450]



# Convert from BGR to RGB
rotation_rgb = cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)
image_original=cv2.cvtColor(image_org, cv2.COLOR_BGR2RGB)
bright=cv2.cvtColor(bright, cv2.COLOR_BGR2RGB)


cv2.imshow('Original Image', image_original)
cv2.imshow('Brightened Image', bright)
cv2.imshow('cropped and Rotated Image', rotation_rgb)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()