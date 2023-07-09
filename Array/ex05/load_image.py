from PIL import Image
import numpy as np

def ft_load(image_path) -> np.ndarray:
    """
    Load an image and convert it to numpy array.
    """
    image = Image.open(image_path)
    image_array = np.array(image)
    print(f"The shape of image is: {image_array.shape}")
    return image_array
