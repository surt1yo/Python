#Students will manipulate color channels of a 
# static image in real-time by pressing specific 
# keys to apply different color filters, including 
# color tints and intensity adjustments. 
# The image will be updated instantly with each key press.
import cv2
import numpy as np

def apply_filter(image, filter_type):
    filter_image_copy=image.copy()
    if filter_type == "red":           
        filter_image_copy[:,:,0]=0 
        filter_image_copy[:,:,1]=0 
    elif filter_type == "green":
        filter_image_copy[:,:,0]=0  
        filter_image_copy[:,:,2]=0 
    elif filter_type == "blue":
        filter_image_copy[:,:,1]=0 
        filter_image_copy[:,:,2]=0 
    elif filter_type == "increase_red":
        filter_image_copy[:,:,2] = cv2.add(filter_image_copy[:,:,2], 60)
    elif filter_type == "decrease_blue":
        filter_image_copy[:,:,0] = cv2.subtract(filter_image_copy[:,:,0], 60)
    elif filter_type == "original": 
        return filter_image_copy
    return filter_image_copy


# Read the image
image = cv2.imread("course-2/opencv/opencv1/monk.png")
if image is None:
    print("Error: Could not load image.")
    exit()
# Create a copy of the original image to apply filters
filtered_image = image.copy()
filter_type = "original"
print("Press 'r' for Red Tint,\n'g' for Green Tint,\n'b' for Blue Tint,\n"
      "'i' for Increase Intensity in Red,\n'd' for Decrease Intensity in Blue," 
      "\n'o' for Original,\n'q' to Quit.")
while True:
    filtered_image = apply_filter(image, filter_type)
    cv2.imshow("Filtered Image", filtered_image)
    key = cv2.waitKey(0) & 0xFF
    if key == ord('r'):
        filter_type = "red"
    elif key == ord('g'):
        filter_type = "green"
    elif key == ord('b'):
        filter_type = "blue"
    elif key == ord('i'):
        filter_type = "increase_red"
    elif key == ord('d'):
        filter_type = "decrease_blue"
    elif key == ord('o'):
        filter_type = "original"
    elif key == ord('q'):
        break
    else:
        print("Invalid key. Please try again.")
        continue
    
cv2.destroyAllWindows()   
    