"""Experiment 39: Reverse video in slow motion"""
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

cap = cv2.VideoCapture(VIDEO_PATH)
frames = []
if not cap.isOpened(): raise FileNotFoundError(VIDEO_PATH)
while True:
    ret, frame = cap.read()
    if not ret: break
    frames.append(frame)
cap.release()
for frame in reversed(frames):
    cv2.imshow("Reverse Slow Motion (q to quit)", frame)
    if cv2.waitKey(150) & 0xFF == ord("q"): break
cv2.destroyAllWindows()
