"""Experiment 18: Crop copy paste ROI"""
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
h, w = image.shape[:2]
roi = image[h//4:3*h//4, w//4:3*w//4].copy()
result = image.copy()
rh, rw = roi.shape[:2]
result[0:rh, 0:rw] = roi
cv2.imshow("Original", image)
cv2.imshow("ROI", roi)
show("ROI pasted at top-left", result)
