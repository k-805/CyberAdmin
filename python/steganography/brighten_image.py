
# Import the Image class from the PIL library part of Pillow
from PIL import Image

    # You call .open function to read the image from the file and .load to read the image into memory
filename = "starr_bears.jpg"
filepath = f"./{filename}"
print(f"The image file path is: {filepath}")

    # Load image and show some properties
original_image = Image.open(filepath)
width, height = original_image.size
mode = original_image.mode

    # Print filename, width, height and mode
print(f"Image name: {filename}")
print(f"Original size: {width} x {height}")
print(f"Mode: {mode}")

# original_image.show()

# original_image.rotate(45).show()

# size = 128, 128
# original_image.thumbnail(size)
# original_image.save(filename + ".thumbnail", "JPEG")

    # Load all pixels
original_pixel_map = original_image.load()

    # The image.new() function --> creates a new image
    # Set mode, width, and height
    # Use original image properties
new_image = Image.new(mode, (width, height))

    # Load all pixels from the new image
new_pixel_map = new_image.load()

    # Move all original pixels into the new map
for col in range(height):
    for row in range(width):
        new_pixel_map[row, col] = original_pixel_map[row, col]

brightness_scalar = 1.5
for y in range(height):
    for x in range(width): 
        # multiply all red and green and blue by the brightness_scalar in the new pixel map

        # to cast an int in python use: int(value)
        original_pixel = original_pixel_map[x, y]
        new_pixel = (int(original_pixel[0]*brightness_scalar), int(original_pixel[1]*brightness_scalar), int(original_pixel[2]*brightness_scalar))
        new_pixel_map[x, y] = new_pixel
        

new_image.show()

# save the new image
new_filename = f"modified_{filename}"
new_filepath = f"./{new_filename}"
new_image.save(new_filepath)