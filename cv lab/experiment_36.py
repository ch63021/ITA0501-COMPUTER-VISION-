"""Experiment 36: Select background by HSV color range"""
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

image = read_image()
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
print("This sample selects low-saturation bright pixels as a background example.")
mask = cv2.inRange(hsv, np.array([0,0,170]), np.array([180,80,255]))
result = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Original", image)
show("Selected Background Color", result)
