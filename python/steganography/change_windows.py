
# Import the Image class from the PIL library part of Pillow
from PIL import Image

    # You call .open function to read the image from the file and .load to read the image into memory
filename = "house.jpg"
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

        # CHANGE WINDOW COLORS
    # FIRST WINDOW 
for y in range(83, 129):
    for x in range(317, 365): 
        original_pixel = original_pixel_map[x, y]
        new_pixel = (255, 0, 0)
        new_pixel_map[x, y] = new_pixel

    # SECOND WINDOW 
for y in range(83, 129):
    for x in range(369, 417): 
        original_pixel = original_pixel_map[x, y]
        new_pixel = (0, 255, 0)
        new_pixel_map[x, y] = new_pixel

    # THIRD WINDOW 
for y in range(83, 129):
    for x in range(420, 465): 
        original_pixel = original_pixel_map[x, y]
        new_pixel = (0, 0, 255)
        new_pixel_map[x, y] = new_pixel
        

new_image.show()
