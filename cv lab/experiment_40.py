
"""Experiment 40: Extract text from video using OCR"""

import os
import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

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

if not cap.isOpened():
    raise FileNotFoundError("Could not open video: " + VIDEO_PATH)

print("Tesseract Version:", pytesseract.get_tesseract_version())
print("Extracting text from video...")

frame_no = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    if frame_no % 5 == 0:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        text = pytesseract.image_to_string(gray)

        if text.strip():
            print("Frame", frame_no, ":", text.strip())

        cv2.imshow("Video OCR", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    frame_no += 1

cap.release()
cv2.destroyAllWindows()

print("OCR Processing Completed")
