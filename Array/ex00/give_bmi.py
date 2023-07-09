import numpy as np


def give_bmi(height, weight):
    """
    This function accepts two lists of integers or floats representing
        heights and weights.
    It calculates the BMI for each height-weight pair and
        returns a list of BMIs.
    If the input lists are not the same length, it raises a ValueError.
    If the lists contain elements that are not int or float,
        it raises a TypeError.
    """
    # Check if both lists are of same length
    if len(height) != len(weight):
        raise ValueError("Lists are not of the same size")

    # Convert list to numpy array for easier computation
    height_np = np.array(height)
    weight_np = np.array(weight)

    # Check if the lists contain only int or float
    if (not issubclass(height_np.dtype.type, np.integer) and
            not issubclass(height_np.dtype.type, np.floating)):
        raise TypeError("Height list should contain only integers or floats")
    if (not issubclass(weight_np.dtype.type, np.integer) and
            not issubclass(weight_np.dtype.type, np.floating)):
        raise TypeError("Weight list should contain only integers or floats")

    # Calculate BMI and return as list
    bmi = weight_np / (height_np**2)
    return bmi.tolist()


def apply_limit(bmi, limit):
    """
    This function accepts a list of integers or floats representing BMIs and
        an integer representing a limit.
    It checks each BMI against(aykırı) the limit and returns
        a list of booleans.
        True if the BMI is above the limit, False otherwise.
    If the list contains elements that are not int or float,
        it raises a TypeError.
    """
    # Convert list to numpy array for easier computation (kıyaslama)
    bmi_np = np.array(bmi)

    # Check if the list contains only int or float
    if (not issubclass(bmi_np.dtype.type, np.integer) and
            not issubclass(bmi_np.dtype.type, np.floating)):
        raise TypeError("BMI list should contain only integers or floats")

    # Apply limit and return as list of booleans
    # Comparison because it is an np array
    result = bmi_np > limit
    return result.tolist()
