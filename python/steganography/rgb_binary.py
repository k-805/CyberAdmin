from PIL import Image

filename = "snake.jpg"
filepath = f"./{filename}"

original_image = Image.open(filepath)

    # load all the pixels from the image into memory
original_pixel_map = original_image.load()


    # show all pixel values that are divisible by 1000 on the x value and divisible by 500 on the y value
for col in range(480):
    for row in range(760):
        pixel = original_pixel_map[row, col]
        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]
        print(f"{row},{col} -- Red: {red:08b} Green: {green:08b} Blue: {blue:08b}" + "\n")


