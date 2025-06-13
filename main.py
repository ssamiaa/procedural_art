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

def rgb_shift(image, shift_amount=5):
    """Applies an RGB channel shift effect for glitch-style visuals."""
    r, g, b = image.split()

    r = r.transform(r.size, Image.AFFINE, (1, 0, shift_amount, 0, 1, 0))
    b = b.transform(b.size, Image.AFFINE, (1, 0, -shift_amount, 0, 1, 0))


    return Image.merge("RGB", (r, g, b))

glitch = rgb_shift(image, shift_amount=10)
glitch.save(os.path.join(OUTPUT_PATH, "rgb_shift.png"))

print("Glitch filter applied and saved.")
def pixel_sort(image):
    """Applies pixel sorting based on brightness within each row."""
    img_np = np.array(image)
    sorted_img = np.copy(img_np)

    for y in range(img_np.shape[0]): 
        row = img_np[y]

        sorted_row = sorted(row, key=lambda pixel: np.mean(pixel))
        sorted_img[y] = sorted_row

    return Image.fromarray(sorted_img)

sorted_image = pixel_sort(image)
sorted_image.save(os.path.join(OUTPUT_PATH, "pixel_sort.png"))

print("Pixel sorting filter applied and saved.")

