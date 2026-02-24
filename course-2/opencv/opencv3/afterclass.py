# Learn how to apply annotation techniques 
# to measure and visualize image width using
#  bi-directional arrows. This project reinforces 
# the concepts of drawing geometric shapes, 
# adding annotations, and understanding dimensions in images.

import cv2
import numpy as np

image = cv2.imread("course-2\opencv\opencv1\monk.png")
if image is None:
    print("Error: Could not load image.")
    exit()

height, width = image.shape[:2]
y_position = height // 2
padding = 20
left_point = (padding, y_position)
right_point = (width - padding, y_position)

arrow_color = (0, 255, 0)
cv2.arrowedLine(
    image,
    left_point,
    right_point,
    arrow_color,
    thickness=2,
    tipLength=0.03
)

cv2.arrowedLine(
    image,
    right_point,
    left_point,
    arrow_color,
    thickness=2,
    tipLength=0.03
)

cv2.line(image, (padding, y_position - 30), (padding, y_position + 30), arrow_color, 2)
cv2.line(image, (width - padding, y_position - 30), (width - padding, y_position + 30), arrow_color, 2)

measured_width = width - (2 * padding)
label = f"Width: {measured_width} px"
(text_width, text_height), _ = cv2.getTextSize(
    label,
    cv2.FONT_HERSHEY_SIMPLEX,
    0.7,
    2
)

text_x = (width - text_width) // 2
text_y = y_position - 40

cv2.putText(
    image,
    label,
    (text_x, text_y),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.7,
    (255, 0, 0),
    2
)

cv2.imshow("Width Measurement", image)
cv2.waitKey(0)
cv2.destroyAllWindows()