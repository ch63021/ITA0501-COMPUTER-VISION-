"""Experiment 34: Draw circle on white image"""
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

h = int(input("Enter image height: "))
w = int(input("Enter image width: "))
if h < 10 or w < 10: raise ValueError("Enter dimensions of at least 10")
image = np.full((h,w,3), 255, dtype=np.uint8)
cv2.circle(image, (w//2,h//2), max(1,min(w,h)//4), (255,0,0), 3)
show("Circle", image)
