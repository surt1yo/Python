# Extend the real-time color filter 
# application by adding new features, 
# such as adjusting the intensity of 
# each color channel dynamically, 
# experimenting with custom key presses, 
# and saving images with applied filters.
import cv2
import numpy as np

def apply_filter(image, filter_type, intensity=0):
    filter_image_copy = image.copy()
    if filter_type == "red":           
        filter_image_copy[:,:,0] = 0 
        filter_image_copy[:,:,1] = 0 
    elif filter_type == "green":
        filter_image_copy[:,:,0] = 0  
        filter_image_copy[:,:,2] = 0 
    elif filter_type == "blue":
        filter_image_copy[:,:,1] = 0 
        filter_image_copy[:,:,2] = 0 
    elif filter_type == "increase_red":
        filter_image_copy[:,:,2] = cv2.add(filter_image_copy[:,:,2], 60 + intensity)
    elif filter_type == "decrease_blue":
        filter_image_copy[:,:,0] = cv2.subtract(filter_image_copy[:,:,0], 60 + intensity)
    elif filter_type == "grayscale":
        filter_image_copy = cv2.cvtColor(filter_image_copy, cv2.COLOR_BGR2GRAY)
        filter_image_copy = cv2.cvtColor(filter_image_copy, cv2.COLOR_GRAY2BGR)
    elif filter_type == "original": 
        return filter_image_copy
    return filter_image_copy


# Read the image
image = cv2.imread("course-2/opencv/opencv1/monk.png")
if image is None:
    print("Error: Could not load image.")
    exit()

filtered_image = image.copy()
filter_type = "original"
intensity = 0
file_counter = 0

print("Press 'r' for Red,\n'g' for Green,\n'b' for Blue,\n"
      "'i' to increase intensity,\n'd' to decrease intensity,\n"
      "'y' for Grayscale,\n'o' for Original,\n's' to save,\n'q' to Quit.")

while True:
    filtered_image = apply_filter(image, filter_type, intensity)
    cv2.imshow("Filtered Image", filtered_image)
    key = cv2.waitKey(0) & 0xFF
    
    if key == ord('r'):
        filter_type = "red"
    elif key == ord('g'):
        filter_type = "green"
    elif key == ord('b'):
        filter_type = "blue"
    elif key == ord('i'):
        intensity = min(intensity + 10, 100)
        print(f"Intensity increased to: {intensity}")
    elif key == ord('d'):
        intensity = max(intensity - 10, 0)
        print(f"Intensity decreased to: {intensity}")
    elif key == ord('y'):
        filter_type = "grayscale"
    elif key == ord('o'):
        filter_type = "original"
        intensity = 0
    elif key == ord('s'):
        filename = f"filtered_image_{file_counter}.png"
        cv2.imwrite(filename, filtered_image)
        print(f"Image saved as: {filename}")
        file_counter += 1
    elif key == ord('q'):
        break
    else:
        print("Invalid key. Please try again.")
        continue
    
cv2.destroyAllWindows() 