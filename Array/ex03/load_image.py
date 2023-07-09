from PIL import Image

def load_image(path: str):
    """
    Load an image file from the provided file path.
    Convert the image to grayscale.
    Return the image object.
    """
    try:
        image = Image.open(path).convert("L")
        return image
    except IOError:
        print("Error: Unable to open image file. Please check the file path.")
        return None
