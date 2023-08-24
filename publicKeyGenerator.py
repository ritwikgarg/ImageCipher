# Program: publicKeyGenerator.py
# This program requests an image from a url and saves it locally. 
# Additionally, it renames the image name in order to prevent
# images being overwritten.


import urllib.request
import os
import re
import urllib.request

def save_image_from_url(url, file_name):
    try:
        urllib.request.urlretrieve(url, file_name)
        print("Image saved as", file_name)
    except Exception as e:
        print("Error:", e)

# URL of the image
image_url = "https://picsum.photos/256/256/?random"

# File name for the image
image_file_name = "pub.png"

# Request and save the image from the URL
save_image_from_url(image_url, image_file_name)

