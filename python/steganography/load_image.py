    # import the image class from the PIL library part of Pillow
from PIL import Image

    # you call .open function to read the image from the file and .load to read the image
    # into memory
filename = "starr_bears.jpg"
filepath = f"./{filename}"
print(f"The image file path is: {filepath}" + "\n")

    # load image and show some properties
original_image = Image.open(filepath)
width, height = original_image.size
mode = original_image.mode
print(f"Original image name: {filename}" + "\n" +
      f"Original image size: {width} x {height}" + "\n" +
      f"Original image mode: {mode}")

    # shows image
original_image.show()

    # converts image into thumbnail
size = 128, 128
original_image.thumbnail(size)
original_image.save(filename + ".thumbnail", "JPEG")