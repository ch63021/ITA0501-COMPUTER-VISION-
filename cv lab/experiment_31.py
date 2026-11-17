"""Experiment 31: Threshold image segmentation"""
import os
import cv2
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGE_PATH = os.path.join(ROOT, "assets", "image.jpg")
VIDEO_PATH = os.path.join(ROOT, "assets", "video.avi")

def read_image(mode=cv2.IMREAD_COLOR):
    image = cv2.imread(IMAGE_PATH, mode)
    if image is None:
        raise FileNotFoundError("Could not read: " + IMAGE_PATH)
    return image

def show(title, image):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image = read_image(cv2.IMREAD_GRAYSCALE)
value = int(input("Enter threshold (0-255): "))
value = max(0, min(255, value))
_, result = cv2.threshold(image, value, 255, cv2.THRESH_BINARY)
cv2.imshow("Original", image)
show("Threshold Segmentation", result)
