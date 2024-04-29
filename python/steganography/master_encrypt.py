from PIL import Image



def get_lsb(int_value):
    return int_value & 1

# def flip_lsb(int_value):
#     return int_value ^ 1

# def string_to_binary_array(input_string):
#     binary_array = []
#     for char in input_string:
#         ascii_value = ord(char)
#         binary_array.extend([int(bit) for bit in bin(ascii_value)[2:].zfill(8)])
#     return binary_array



filename = 'contains_hidden_message_starr_bears.jpg'
filepath = f"./{filename}"

# Load the original image, and get its size and color mode.
orig_image = Image.open(filepath)
width, height = orig_image.size
mode = orig_image.mode

# Show information about the original image.
print(f"Original image: {filename}")
print(f"Size: {width} x {height} pixels")
print(f"Mode: {mode}")

orig_pixel_map = orig_image.load()

user_input = input("how many characters is the secret message: ")
message_len = int(user_input)
pixels_to_process = message_len * 3



binary_list = []

for x in range(1): 
    for y in range(pixels_to_process): 
        pixel = orig_pixel_map[x, y]

        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]

        lsb_red = int(get_lsb(red))
        lsb_green = int(get_lsb(green))
        lsb_blue = int(get_lsb(blue))

        binary_list.append(lsb_red)
        binary_list.append(lsb_green)
        binary_list.append(lsb_blue)

# print(f"binary list: {binary_list}")

binary_string = ''.join(map(str, binary_list))

print(f"{binary_string}")


len_bin = len(binary_string)
letters = [binary_string[i:i+8] for i in range(0, len_bin, 8)]

# for l in letters: 
#     print(f"{l}")


ascii_chars = [chr(int(letter, 2)) for letter in letters]

ascii_string = ''.join(ascii_chars)
print(f"Your message is: {ascii_string}")
