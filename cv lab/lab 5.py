
import cv2
import os
import matplotlib.pyplot as plt

def analyze_histogram(image):
    colors = ("b", "g", "r")
    for i, color in enumerate(colors):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
    plt.title("Color Histogram")
    plt.xlabel("Color Intensity")
    plt.ylabel("Number of Pixels")
    plt.xlim([0, 256])
    plt.show()

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
    analyze_histogram(image)
