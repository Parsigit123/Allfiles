from PIL import Image

# Belongs to Camera02.py

def convert_image(input_image):
    """Gets a PIL image file and returns its grayscale version"""
    img = Image.open(input_image)
    gray_img = img.convert('L')
    return gray_img # ADDING THIS LINE FIXES THE BUG