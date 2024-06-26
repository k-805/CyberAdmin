from PIL import Image



def get_lsb(int_value):
    return int_value & 1

def flip_lsb(int_value):
    return int_value ^ 1

def string_to_binary_array(input_string):
    binary_array = []
    for char in input_string:
        ascii_value = ord(char)
        binary_array.extend([int(bit) for bit in bin(ascii_value)[2:].zfill(8)])
    return binary_array



filename = 'starr_bears.jpg'
filepath = f"./{filename}"

orig_image = Image.open(filepath)
width, height = orig_image.size
mode = orig_image.mode

# Show information about the original image.
# print(f"Original image: {filename}")
# print(f"Size: {width} x {height} pixels")
# print(f"Mode: {mode}")



orig_pixel_map = orig_image.load()
new_image = Image.new(mode, (width, height))
new_pixel_map = new_image.load()

for x in range(width):
    for y in range(height):        
        new_pixel_map[x, y] = orig_pixel_map[x, y]




user_input = input("Enter a string to be encrypted: ") # Collect a string from the user
message_length = len(user_input)
print("You entered:", user_input) # Print the collected string
input_binary = string_to_binary_array(user_input)


# print("String:", user_input)
# print("Binary Array:", input_binary)
# print("\nPixel data:")


binary_input_length = len(user_input)
binary_input_index = 0
new_red = 0
new_blue = 0
new_green = 0
new_pixel = (0, 0, 0)
all_input_processed = False



for x in range(width):
    for y in range(height): 
        pixel = new_pixel_map[x, y]
        print(f"{pixel}")

        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]

        new_red = red
        lsb_red = get_lsb(red)

        if lsb_red != input_binary[binary_input_index]: 
            new_red = flip_lsb(red)
        binary_input_index += 1     # Advances index whether we flipped a bit or not
        
        # If there are no more bits in binary input, we are done
        if binary_input_index == binary_input_length: 
            new_pixel = (new_red, green, blue)
            new_pixel_map[x, y] = new_pixel
            all_input_processed = True
            break       # breaks out of inner loop



        new_green = green
        lsb_green = get_lsb(green)

        if lsb_green != input_binary[binary_input_index]: 
            new_green = flip_lsb(green)
        binary_input_index += 1

        if binary_input_index == binary_input_length: 
            new_pixel = (new_red, new_green, blue)
            new_pixel_map[x, y] = new_pixel
            all_input_processed = True
            break



        new_blue = blue
        lsb_blue = get_lsb(blue)
        
        if lsb_blue != input_binary[binary_input_index]: 
            flip_lsb(blue)
        binary_input_index += 1

        if binary_input_index == binary_input_length: 
            new_pixel = (new_red, new_green, new_blue)
            new_pixel_map[x, y] = new_pixel
            all_input_processed = True
            break
        else: 
            new_pixel = (new_red, new_green, new_blue)
            new_pixel_map[x, y] = new_pixel
    
    if all_input_processed: 
            break



new_filename = f'contains_hidden_message_{filename}'
new_filepath = f'./{new_filename}'
new_image.save(new_filepath, 'PNG')  # must do this, or the jpg is not the correct map

print(f'Your messages has been encrypted in: {new_filepath}')
print(f'{message_length} characters have been encrypted')