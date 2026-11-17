"""Experiment 32: White image with four corner boxes"""
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
if h < 10 or w < 10: raise ValueError("Height and width must be at least 10")
image = np.full((h,w,3), 255, dtype=np.uint8)
bh, bw = h//10, w//10
image[:bh,:bw] = (0,0,0)
image[:bh,w-bw:] = (255,0,0)
image[h-bh:,:bw] = (0,255,0)
image[h-bh:,w-bw:] = (0,0,255)
show("Four Colored Boxes", image)
