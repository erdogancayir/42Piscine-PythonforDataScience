import numpy as np

def slice_me(family, start, end):
    """
    This function accepts a 2D list (family), and two integers (start and end) representing the range to slice the list.
    It prints the shape of the original 2D list and the shape of the sliced list.
    Then, it returns the sliced list.
    If the input is not a 2D list, it raises a ValueError.
    """
    # Convert the list to a numpy array for easy manipulation
    family_np = np.array(family)

    # Check if the input is a 2D list
    if family_np.ndim != 2:
        raise ValueError("Input should be a 2D list")

    # Print the shape of the original array
    print("My shape is :", family_np.shape)

    # Perform slicing
    sliced_family = family_np[start:end]

    # Print the shape of the sliced array
    print("My new shape is :", sliced_family.shape)

    # Convert the sliced numpy array back to a list and return
    return sliced_family.tolist()
