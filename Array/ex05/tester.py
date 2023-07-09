import matplotlib.pyplot as plt
from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey

# Loading the image
array = ft_load("landscape.jpg")

# Apply invert and display the result
array = ft_invert(array)
plt.imshow(array)
plt.title('Inverted')
plt.show()

# Apply red and display the result
array = ft_red(array)
plt.imshow(array)
plt.title('Red')
plt.show()

# Apply green and display the result
array = ft_green(array)
plt.imshow(array)
plt.title('Green')
plt.show()

# Apply blue and display the result
array = ft_blue(array)
plt.imshow(array)
plt.title('Blue')
plt.show()

# Apply grey and display the result
array = ft_grey(array)
plt.imshow(array, cmap='gray')  # Grayscale image needs a gray colormap
plt.title('Grey')
plt.show()

print(ft_invert.__doc__)
