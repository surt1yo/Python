# This activity involves annotating an image using OpenCV by 
# drawing rectangles and circles to highlight
#regions of interest, connecting them with a line, 
# and visualizing the image height using bi-directional arrows. 
#Text annotations are added for clarity, 
# making the image informative and visually structured.
import cv2
import matplotlib.pyplot as plt

# Step 1: Load the Image
image = cv2.imread("course-2\opencv\opencv1\monk.png")
# Convert BGR to RGB for correct color display with matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# Get image dimensions
h,w,_ = image_rgb.shape

# Step 2: Draw Two Rectangles Around Interesting Regions
# Rectangle 1: Top-left corner
rh,rw=100,80
top_left=(30,30)
bottom_right=(30+rw,30+rh)
cv2.rectangle(image_rgb, top_left, bottom_right, (255,255,0), 3)
cx=top_left[0]+rw//2
cy=top_left[1]+rh//2
cv2.circle(image_rgb, (cx, cy), 6, (0, 255, 0), -1) 



# Rectangle 2: Bottom-right corner

rh1,rw1=100,150
top_left1=(w-30-rw1,h-30-rh1)
bottom_right1=(w-30,h-30)
cv2.rectangle(image_rgb, top_left1, bottom_right1, (255,0,255), 3)
cx1=top_left1[0]+rw1//2
cy1=top_left1[1]+rh1//2
cv2.circle(image_rgb, (cx1, cy1),7, (0,255,255), -1)

# Step 4: Draw Connecting Lines Between Centers of Rectangles
cv2.line(image_rgb, (cx, cy), (cx1,cy1), (255,0,0), 2)

# Step 5: Add Text Labels for Regions and Centers
#cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType, bottomLeftOrigin)

cv2.putText(image_rgb, "Rectangle 1", (top_left[0], top_left[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,0), 1,cv2.LINE_AA)
cv2.putText(image_rgb, "Center 1", (cx - 20, cy - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1, cv2.LINE_AA)
cv2.putText(image_rgb, "Rectangle 2", (top_left1[0], top_left1[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,255), 1,cv2.LINE_AA)
cv2.putText(image_rgb, "Center 2", (cx1 - 20, cy1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,255), 1, cv2.LINE_AA)

# : Display the Annotated Image
plt.imshow(image_rgb)
plt.title('Annotated Image with Regions, Centers, and Bi-Directional Height Arrow')
plt.axis('off')
plt.show()