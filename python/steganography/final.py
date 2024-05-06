# The code will change portions of the image to red and brighten the overall image

from PIL import Image



def change_color(): 
    for y in range(10, 100):
        for x in range(100, 150): 
            new_pixel = (255, 0, 0)
            new_pixel_map[x, y] = new_pixel
    for y in range(10, 100):
        for x in range(300, 350): 
            new_pixel = (255, 0, 0)
            new_pixel_map[x, y] = new_pixel
    
    for y in range(150, 200):
        for x in range(50, 100): 
            new_pixel = (255, 0, 0)
            new_pixel_map[x, y] = new_pixel
    for y in range(200, 250):
        for x in range(100, 150): 
            new_pixel = (255, 0, 0)
            new_pixel_map[x, y] = new_pixel
    for y in range(200, 250):
        for x in range(150, 200): 
            new_pixel = (255, 0, 0)
            new_pixel_map[x, y] = new_pixel
    for y in range(200, 250):
        for x in range(200, 250): 
            new_pixel = (255, 0, 0)
            new_pixel_map[x, y] = new_pixel
    for y in range(200, 250):
        for x in range(250, 300): 
            new_pixel = (255, 0, 0)
            new_pixel_map[x, y] = new_pixel
    for y in range(200, 250):
        for x in range(300, 350): 
            new_pixel = (255, 0, 0)
            new_pixel_map[x, y] = new_pixel
    for y in range(150, 200):
        for x in range(350, 400): 
            new_pixel = (255, 0, 0)
            new_pixel_map[x, y] = new_pixel

def change_brightness(): 
    brightness_scalar = 1.5
    for y in range(height):
        for x in range(width): 
            original_pixel = original_pixel_map[x, y]
            new_pixel = (int(original_pixel[0]*brightness_scalar), int(original_pixel[1]*brightness_scalar), int(original_pixel[2]*brightness_scalar))
            new_pixel_map[x, y] = new_pixel



filename = "snake.jpg"
filepath = f"./{filename}"
print(f"The image file path is: {filepath}")

original_image = Image.open(filepath)
width, height = original_image.size
mode = original_image.mode

original_pixel_map = original_image.load()
new_image = Image.new(mode, (width, height))
new_pixel_map = new_image.load()


for col in range(height):
    for row in range(width):
        new_pixel_map[row, col] = original_pixel_map[row, col]


change_brightness()
change_color()


new_filename = "modified_snake.png"
new_filepath = f"./{new_filename}"
new_image.save(new_filepath)