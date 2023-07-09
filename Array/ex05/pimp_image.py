import numpy as np

def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the color of the image received.
    """
    return 255 - array

def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Enhances the red color in the image.
    """
    array[..., 0] *= 2  # Multiplying red channel by 2
    return array

def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Reduces the green color in the image.
    """
    array[..., 1] -= 50  # Subtracting 50 from green channel
    return array

def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Set the blue color in the image to maximum.
    """
    array[..., 2] = 255  # Setting blue channel to 255
    return array

def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Converts the image to grayscale.
    """
    return np.dot(array[...,:3], [0.2989, 0.5870, 0.1140])
