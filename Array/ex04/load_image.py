from PIL import Image
import numpy as np

def load_image(image_path):
    """ 
    Loads an image from the specified path.

    Args:
        image_path (str): The path to the image file.

    Returns:
        PIL.Image.Image or None: The loaded image as a PIL Image object if successful, 
                                 otherwise returns None.

    Raises:
        None.
    """
    try:
        return Image.open(image_path)
    except IOError:
        print(f"Unable to open image {image_path}. Please check the path.")
        return None