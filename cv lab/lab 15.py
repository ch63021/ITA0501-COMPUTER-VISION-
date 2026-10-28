
import cv2
import os
import numpy as np

folder = os.path.dirname(os.path.abspath(__file__))
image = None

for file in os.listdir(folder):
    if file.lower().endswith((".jpg", ".jpeg", ".png")):
        image = cv2.imread(os.path.join(folder, file))
        if image is not None:
            break

if image is None:
    print("Image not found")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    corners = cv2.cornerHarris(gray, 2, 3, 0.04)
    image[corners > 0.01 * corners.max()] = [0, 0, 255]

    cv2.imshow("Harris Corner Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
