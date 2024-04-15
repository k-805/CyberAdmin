from PIL import Image

filename = "starr_bears.jpg"
filepath = f"./{filename}"
print(f"The image file path is: {filepath}" + "\n")

original_image = Image.open(filepath)

    # load all the pixels from the image into memory
original_pixel_map = original_image.load()

    # look at first pixel at top left corner
first_pixel = original_pixel_map[0,0]
print(f"First pixel: {first_pixel}")

    # take data out of first_pixel
original_red = first_pixel[0]
original_green = first_pixel[1]
original_blue = first_pixel[2]
# print(f"Original Red: {original_red}" + "\n" +
#       f"Original Green: {original_green}" + "\n" +
#       f"Oringinal Blue: {original_blue}")

    # print showing binary values all with 8 bits
print(f"Red: {original_red:08b} Green: {original_green:08b} Blue: {original_blue:08b}" + "\n")

    # show/print out all pixel as (r, g, b) tuple
# for row in range(1560):
#    for col in range(811):
#        pixel = original_pixel_map[row, col]
#        print(pixel)


# last_pixel = original_pixel_map[1559,810]
# before_last = original_pixel_map[1559,809]
# before_before_last = original_pixel_map[1559,808]
# print(f"Last pixel: {last_pixel}")
# print(f"Last-1 pixel: {before_last}")
# print(f"Last-2 pixel: {before_before_last}")

    # show pixel value (rgb) for pixel: (867, 432)
for row in range(1560):
    for col in range(811):
        pixel = original_pixel_map[row, col]

        if (row == 867 and col == 432):
            print(f"{row},{col} == {pixel}" + "\n")
            break

    # show all pixel values that are divisible by 1000 on the x value and divisible by 500 on the y value
for col in range(811):
    for row in range(1560):
        pixel = original_pixel_map[row, col]

        if (row % 1000 == 0 and col % 500 == 0 ):
            print(f"{row},{col} == {pixel}")
            break

