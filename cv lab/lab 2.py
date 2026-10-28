
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
    blur = cv2.GaussianBlur(image, (15, 15), 0)
    cv2.imshow("Original Image", image)
    cv2.imshow("Blurred Image", blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
