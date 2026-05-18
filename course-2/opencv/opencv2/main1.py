# Rotate an image by 45 degrees and adjust its 
# brightness to see the effects of basic 
# arithmetic operations on images.
import cv2
import matplotlib.pyplot as plt


image=cv2.imread("course-2\opencv\opencv1\monk.png")
image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
h,w=image.shape[:2] #return h and w but the first value is width
c=(w//2,h//2)
print(c)
m=cv2.getRotationMatrix2D(c,45,1)
# Rotate the image by 45 degrees
rotated_image=cv2.warpAffine(image,m,(w,h))

r_rgb=cv2.cvtColor(rotated_image,cv2.COLOR_BGR2RGB)
plt.imshow(r_rgb)
plt.title("Rotated Image")
plt.show()

# Increase brightness by adding 50 to all pixel values
# Use cv2.add to avoid negative values or overflow
brightness_matrix = np.ones(image.shape, dtype="uint8") * 50
brighter = cv2.add(image, brightness_matrix)

brighter_rgb = cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)
plt.imshow(brighter_rgb)
plt.title("Brighter Image")
plt.show()