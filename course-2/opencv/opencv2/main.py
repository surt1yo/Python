# Convert an image from BGR to RGB and grayscale, then crop a region of interest.
import cv2
import matplotlib.pyplot as plt


image=cv2.imread("course-2\opencv\opencv1\monk.png")

rgb_image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(rgb_image)
plt.title("RGB IMAGE")
plt.show()

grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(grey_image)
plt.title("gray scale")
plt.show()


# Cropping the image
# Assume we know the region we want: rows 100 to 300, columns 200 to 400
cropped_image = image[100:300, 200:400]
cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("Cropped Region")
plt.show()