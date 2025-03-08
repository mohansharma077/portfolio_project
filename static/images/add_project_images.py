# This script demonstrates how to create placeholder images for your Django portfolio
# You would run this once to generate the images, or manually add images to your static/images directory

import os
from PIL import Image, ImageDraw, ImageFont
import random

# Define the directory where images will be saved
image_dir = "static/images"
os.makedirs(image_dir, exist_ok=True)

# Define image sizes
featured_size = (1200, 600)
project_size = (600, 400)

# Define color palettes (modern, vibrant colors)
color_palettes = [
    [(41, 128, 185), (52, 152, 219), (155, 89, 182)],  # Blue/Purple
    [(230, 126, 34), (231, 76, 60), (241, 196, 15)],  # Orange/Red/Yellow
    [(46, 204, 113), (26, 188, 156), (52, 152, 219)],  # Green/Teal/Blue
    [(155, 89, 182), (142, 68, 173), (52, 152, 219)],  # Purple/Blue
    [(52, 73, 94), (44, 62, 80), (189, 195, 199)]  # Dark/Gray
]

# Project themes for the images
project_themes = [
    "E-commerce Platform",
    "Weather Dashboard",
    "Fitness Tracker App",
    "Portfolio Website",
    "Task Management System",
    "Food Delivery App",
    "Travel Blog"
]


def create_gradient_background(size, colors):
    """Create a gradient background with the given colors"""
    image = Image.new('RGB', size, color=colors[0])
    draw = ImageDraw.Draw(image)

    width, height = size
    for i in range(height):
        # Calculate color for this line
        r = int(colors[0][0] + (colors[1][0] - colors[0][0]) * i / height)
        g = int(colors[0][1] + (colors[1][1] - colors[0][1]) * i / height)
        b = int(colors[0][2] + (colors[1][2] - colors[0][2]) * i / height)
        draw.line([(0, i), (width, i)], fill=(r, g, b))

    return image


def add_overlay_pattern(image, color):
    """Add a subtle pattern overlay"""
    width, height = image.size
    draw = ImageDraw.Draw(image, 'RGBA')

    # Add some random circles for texture
    for _ in range(20):
        x = random.randint(0, width)
        y = random.randint(0, height)
        size = random.randint(10, 100)
        draw.ellipse((x, y, x + size, y + size),
                     fill=(color[0], color[1], color[2], 30))

    return image


def add_text(image, text):
    """Add text to the image"""
    draw = ImageDraw.Draw(image)
    width, height = image.size

    # We'd normally use a proper font here
    # font = ImageFont.truetype("arial.ttf", 36)
    # Since we can't guarantee font availability, we'll use default
    font_size = 36

    # Position text in center
    text_width = len(text) * font_size * 0.6  # Approximate width
    x = (width - text_width) / 2
    y = height / 2 - font_size

    # Add a shadow/outline effect
    for offset in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
        draw.text((x + offset[0], y + offset[1]), text, fill=(0, 0, 0, 180))

    # Draw the main text
    draw.text((x, y), text, fill=(255, 255, 255))

    return image


def create_project_image(filename, size, theme, palette):
    """Create a project image with the given theme and palette"""
    colors = random.choice(palette)

    # Create gradient background
    image = create_gradient_background(size, colors[:2])

    # Add pattern overlay
    image = add_overlay_pattern(image, colors[2])

    # Add text
    image = add_text(image, theme)

    # Save the image
    image.save(os.path.join(image_dir, filename))
    print(f"Created {filename}")


# Create featured project image
create_project_image("featured-project.jpg", featured_size, "E-commerce Platform", color_palettes)

# Create project images
for i, theme in enumerate(project_themes[1:], 1):
    create_project_image(f"project{i}.jpg", project_size, theme, color_palettes)

print("All project images have been created!")