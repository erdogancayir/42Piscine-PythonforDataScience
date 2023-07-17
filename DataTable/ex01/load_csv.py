import pandas as pd


def load(path: str):
    """
    Load a CSV file as a pandas DataFrame.

    Args:
        path (str): The path to the CSV file.

    Returns:
        pd.DataFrame or None: The loaded DataFrame if successful, None otherwise.
    """
    try:
        # Try to load the file
        data = pd.read_csv(path)
        # Print the dimensions of the dataset
        print(f"Loading dataset of dimensions {data.shape}")

        # Return the loaded DataFrame
        return data

    except FileNotFoundError:
        print("The file path provided does not exist.")
        return None
    except pd.errors.ParserError:
        print("There was a problem parsing the file.")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
