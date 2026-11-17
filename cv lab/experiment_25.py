"""Experiment 25: Watch recognition by template matching"""
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
template = cv2.imread(os.path.join(ROOT, "assets", "watch_template.jpg"), cv2.IMREAD_GRAYSCALE)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
if template is None:
    raise FileNotFoundError("watch_template.jpg is missing from assets")
th, tw = template.shape
match = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
_, score, _, loc = cv2.minMaxLoc(match)
if score >= 0.55:
    x, y = loc
    cv2.rectangle(image, (x,y), (x+tw,y+th), (0,255,0), 2)
    print("Watch-like template found; score:", round(score, 3))
else:
    print("No matching watch template found; score:", round(score, 3))
show("Watch Template Matching", image)
