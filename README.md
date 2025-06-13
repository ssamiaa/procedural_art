# Procedural Art Generator (Python)

A beginner-friendly creative coding project using Python and Pillow for procedural image transformations.  
This project explores how to apply basic image filters like Gaussian blur, edge detection, and contour extraction — foundational steps for building generative art tools.

## Features
- Load images and apply visual filters and transform static images
- RGB Channel Shift Animation (GIF)
- Pixelation Filter (adjustable block size)
- Modular setup for adding more advanced effects later (pixel sorting, channel shifting, etc.) and environment effects (e.g. rain, fog, night mode)
- Easily extendable for more advanced effects like pixel sorting, glitch, or stylized overlays


## Requirements
- Python 3.x
- Libraries: Pillow, NumPy, OpenCV (for future effects), Matplotlib

## Preview 

### RGB Channel Shift Animation



<img src="output/rgb_shift_anim.gif" width="400">

### Pixelation Filter


<img src="output/pixelated_anim.gif" width="400">

Install dependencies:
```bash
pip3 install pillow numpy opencv-python matplotlib imageio
