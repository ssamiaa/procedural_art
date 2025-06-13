from PIL import Image, ImageFilter
import numpy as np
import cv2
import os


INPUT_PATH = "input/sample.jpg"
OUTPUT_PATH = "output/"

# Loading image using Pillow
image = Image.open(INPUT_PATH)

# Basic filter examples
blurred = image.filter(ImageFilter.GaussianBlur(4))
edges = image.filter(ImageFilter.FIND_EDGES)
contour = image.filter(ImageFilter.CONTOUR)


blurred.save(os.path.join(OUTPUT_PATH, "blurred.png"))
edges.save(os.path.join(OUTPUT_PATH, "edges.png"))
contour.save(os.path.join(OUTPUT_PATH, "contour.png"))

print("Basic filters applied and saved.")