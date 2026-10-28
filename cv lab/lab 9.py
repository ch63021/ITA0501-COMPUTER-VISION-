
import cv2
import os

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
    bigger = cv2.resize(image, None, fx=2, fy=2)
    smaller = cv2.resize(image, None, fx=0.5, fy=0.5)

    cv2.imshow("Original Image", image)
    cv2.imshow("Bigger Image", bigger)
    cv2.imshow("Smaller Image", smaller)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

