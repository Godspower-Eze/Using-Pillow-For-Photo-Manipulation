from PIL import Image
import os

image1 = Image.open('blur-close-up-code-computer-546819.jpg')
# This creates an image instance
image1.show()
# This displays the image
image1.save('blur-close-up-code-computer-546819.png')
# This saves the image using another
# format ".png" which is not compulsory,
# you could decide to save with the same format

"""
Imagine you wanted to change the sizes of multiple pictures and save them 
in a different location rather than the original format. Let's do that
"""
size_300 = (300, 300)
# This is the tuple that will be used in the resizing of the image to 300x300pixels
size_700 = (700, 700)
# This is the tuple that will be used in the resizing of the image to 700x700pixels
for f in os.listdir():
    # os.listdir() is used to list out all files and
    # folder in a directory and f pickes them and stores them
    if f.endswith('.jpg'):
        # f.endswith('.jpg') is used to find all the files that ends in ".jpg"
        i = Image.open(f)
        # This creates an image instance with every f that endswith ".jpg"
        f_name, f_ext = os.path.splitext(f)
        # This is used to split a file into its filename and its extension
        print(f_name)
        # This prints the filename
        print(f_ext)
        # This prints the extension
        i.save(f'pngs/{f_name}.png')
        # This saves the images in the pngs folder in png
        i.thumbnail(size_300)
        # This resizes the images to 300x300
        i.save(f'300/{f_name}_300.png')
        # This saves the images in the 300 folder in png with an "_300" showing its a 300 sized image
        i.thumbnail(size_700)
        # This resizes the images to 700x700
        i.save(f'700/{f_name}_700.png')
        # This saves the images in the 300 folder in png with an "_300" showing its a 300 sized image

"""
Now Let's see how we could rotate, blur and change a picture to black and white
"""
image1.convert(mode='L').save('black_and_white.png')
image1.rotate(90).save('rotated_image.png')
from PIL import ImageFilter
image1.filter(ImageFilter.GaussianBlur(15)).save('blurred_image.png')
"""
This is just a tip of the iceberg of what can be done with the Pillow library. Keeping creating.....
"""

help(Image)
# Use this for help