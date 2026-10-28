
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
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    equalized = cv2.equalizeHist(gray)

    cv2.imshow("Original Image", gray)
    cv2.imshow("Histogram Equalized Image", equalized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
