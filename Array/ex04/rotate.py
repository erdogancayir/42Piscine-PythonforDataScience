import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from load_image import load_image


def crop_square(image):
    """
    Crops the input image to a square shape.

    Args:
        image (PIL.Image.Image): The input image.

    Returns:
        PIL.Image.Image: The cropped square image.
    """
    width, height = image.size
    new_edge = min(width, height)
    
    left = (width - new_edge) / 2
    top = (height - new_edge) / 2
    right = (width + new_edge) / 2
    bottom = (height + new_edge) / 2

    return image.crop((left, top, right, bottom))


def transpose_image(image):
    """
    Transposes the input image.

    Args:
        image (PIL.Image.Image): The input image.

    Returns:
        PIL.Image.Image: The transposed image.
    """
    image_data = np.array(image)
    transposed_data = [[row[i] for row in image_data] for i in range(len(image_data[0]))]
    return Image.fromarray(np.uint8(transposed_data))


def main():
    """
    Main function that demonstrates cropping and transposing an image.
    """
    image_path = "animal.jpeg"
    img = load_image(image_path)

    if img is None:
        return

    img_cropped = crop_square(img)
    print(f"The shape of image is: {np.array(img_cropped).shape}")
    print(np.array(img_cropped))

    img_transposed = transpose_image(img_cropped)
    print(f"New shape after Transpose: {np.array(img_transposed).shape}")
    print(np.array(img_transposed))

    img_gray = img_transposed.convert('L')
    plt.imshow(img_gray, cmap='gray')
    plt.show()

if __name__ == "__main__":
    main()
