            # THIS PROGRAM WILL

        # collect a message to hide in an image
msg = input("What is the message you want to hide? ")
print(f'Message to be hidden: {msg}')


        # convert the entire message to a binary message with each character consisting of 8-bits
    # step 1, use the ord function to convert each char to an int 
ascii_decimals = [ord(c) for c in msg]
print(f'as ascii decimal your message is: {ascii_decimals}')

    # step 2, ascii to binary
char_binary = [format(ord(c), '08b') for c in msg]
print(f'binary: {char_binary}')

    #loop and show all
for b in char_binary:
    print(f'{b}')

binary_msg = ''.join(format(ord(c), '08b') for c in msg)
print(f'binary: {binary_msg}')

        # get the length of total bits that make up your message



        # verify you have have enough pixels necessary to hide the image and if not, 
        # the program should tell user hiding the message in the image provided cannot be done and that the 
        # user will need to use a "bigger" image. The program should then exit



        # modify each LSB for each color in each pixel, for as many pixels necessary, to hide your binary message in the image.



        # save the image and view and compare to original



        # NOTE: Each pixel will have three available bits to hide your message. These are the LSB for each color.



        # Submit your code, your modified image, your original image, and the message that you encrypted in your modified image.

