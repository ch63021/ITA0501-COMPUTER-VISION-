import cv2
import os

folder = os.path.dirname(os.path.abspath(__file__))

image = None

for file in os.listdir(folder):
    if file.lower().endswith((".jpg", ".jpeg", ".png")):
        image = cv2.imread(os.path.join(folder, file))
        if image is not None:
            print("Image found:", file)
            break

if image is None:
    print("No image found. Check the folder.")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Original Image", image)
    cv2.imshow("Grayscale Image", gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
