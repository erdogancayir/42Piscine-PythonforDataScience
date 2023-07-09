from PIL import Image
import numpy as np

def ft_load(path):
    """
    This function accepts a string representing the path of an image.
    It opens the image, prints its format and its pixel content in RGB format, and then returns the pixel content.
    If the path does not lead to a JPG or JPEG image, it raises a ValueError.
    """
    # Open the image
    try:
        img = Image.open(path)
    except IOError:
        raise ValueError("Cannot open image. Please check the path and the image format.")

    # Check the image format
    if img.format not in ['JPEG', 'JPG']:
        raise ValueError("The image format should be JPG or JPEG")

    # Print the image format
    print(f"The image format is: {img.format}")

    # Convert the image to an RGB array using numpy
    img_np = np.array(img)

    # Print the shape of the image
    print(f"The shape of image is: {img_np.shape}")

    # Return the pixel content in RGB format
    return img_np
