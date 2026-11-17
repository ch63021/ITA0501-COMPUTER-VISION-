"""Experiment 30: Smile detection"""
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
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")
if detector.empty(): raise RuntimeError("Could not load Haar cascade: haarcascade_smile.xml")
objects = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(20,20))
for (x,y,w,h) in objects:
    cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 2)
print("Smiles detected:", len(objects))
show("Smiles Detection", image)
