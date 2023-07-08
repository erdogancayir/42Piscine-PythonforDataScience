import sys


def count_chars(text):
    """
    This function counts and returns the number of upper-case letters,
        lower-case letters, punctuation characters, digits, and
        spaces in the provided text.
    Parameters:
        text (str): The text to be analyzed
    Returns:
        tuple: A tuple containing
        the counts of upper-case letters, lower-case letters,
        punctuation characters,
        spaces, and digits (in that order).
    """
    punctuation_chars = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    upper_letters = sum(1 for c in text if c.isupper())
    lower_letters = sum(1 for c in text if c.islower())
    punctuation = sum(1 for c in text if c in punctuation_chars)
    digits = sum(1 for c in text if c.isdigit())
    spaces = sum(1 for c in text if c.isspace())
    return upper_letters, lower_letters, punctuation, spaces, digits


def main():
    """
    The main function of the script. It retrieves the text
        from the command line arguments or asks
        the user to input it if no arguments are provided.
    Then, it calls count_chars to analyze the text and prints the results.
    """
    if len(sys.argv) > 2:
        raise AssertionError("Please provide only one argument.")
    elif len(sys.argv) == 2:
        text = sys.argv[1]
    else:
        text = input("What is the text to count?\n")
    upper, lower, punct, spaces, digits = count_chars(text)
    total_chars = len(text)
    print(f"The text contains {total_chars} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


if __name__ == '__main__':
    main()
