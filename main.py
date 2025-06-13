from PIL import Image, ImageFilter
import numpy as np
import cv2
import os


INPUT_PATH = "input/sample.jpg"
INPUT_PATH2 = "input/sample2.jpg"
INPUT_PATH3 = "input/sample3.jpg"
OUTPUT_PATH = "output/"

# Loading image using Pillow
image = Image.open(INPUT_PATH)
image2 = Image.open(INPUT_PATH2)
image3 = Image.open(INPUT_PATH3)

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

def generate_rgb_shift_gif(image, frames=10, shift_range=15, output_path="output/rgb_shift_anim.gif"):
    images = []

    for i in range(frames):
        shift = int(np.sin(i / frames * 2 * np.pi) * shift_range)
        r, g, b = image.split()

        r = r.transform(r.size, Image.AFFINE, (1, 0, shift, 0, 1, 0))
        b = b.transform(b.size, Image.AFFINE, (1, 0, -shift, 0, 1, 0))

        img = Image.merge("RGB", (r, g, b)).convert("RGB")  # <- Force RGB mode
        images.append(img)

    images[0].save(output_path, save_all=True, append_images=images[1:], duration=100, loop=0)

generate_rgb_shift_gif(image)

print("Animated RGB Glitch Shift applied and saved.")


def generate_pixelated_gif(image, frames=10, min_block=10, max_block=30, output_path="output/pixelated_anim.gif"):
    images = []

    width, height = image.size

    for i in range(frames):
        block_size = int(
            min_block + (np.sin(i / frames * 2 * np.pi) + 1) / 2 * (max_block - min_block)
        )

        small = image.resize(
            (width // block_size, height // block_size),
            resample=Image.BILINEAR
        )

        pixelated = small.resize((width, height), resample=Image.NEAREST)
        images.append(pixelated.convert("RGB"))

    images[0].save(output_path, save_all=True, append_images=images[1:], duration=100, loop=0)

generate_pixelated_gif(image3)

print("Pixelated Animation applied and saved.")