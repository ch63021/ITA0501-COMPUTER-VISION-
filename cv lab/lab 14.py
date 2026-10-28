
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
    rows, cols = image.shape[:2]

    src = np.float32([
        [0, 0],
        [cols - 1, 0],
        [0, rows - 1],
        [cols - 1, rows - 1]
    ])

    dst = np.float32([
        [50, 50],
        [cols - 50, 0],
        [0, rows - 50],
        [cols - 1, rows - 1]
    ])

    matrix = cv2.getPerspectiveTransform(src, dst)
    result = cv2.warpPerspective(image, matrix, (cols, rows))

    cv2.imshow("Original Image", image)
    cv2.imshow("Perspective Transformation", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
