"""Experiment 35: Add user text to image"""
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
text = input("Enter text to display: ")
cv2.putText(image, text[:60], (20, min(60, image.shape[0]-10)), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)
show("Text on Image", image)
