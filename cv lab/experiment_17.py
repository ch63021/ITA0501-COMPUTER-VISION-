"""Experiment 17: Add watermark"""
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
overlay = image.copy()
cv2.putText(overlay, "CV LAB", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,255), 2)
result = cv2.addWeighted(overlay, 0.3, image, 0.7, 0)
show("Watermarked Image", result)
