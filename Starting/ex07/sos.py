import sys

NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
    "0": "----- "
}


def morse_encode(message):
    """
    Encode the given message into Morse Code.

    Args:
        message (str): The message to be encoded.

    Returns:
        str: The encoded Morse Code.

    Raises:
        AssertionError: If the message contains invalid characters.
    """
    morse_code = ""
    for char in message:
        char = char.upper()
        if char in NESTED_MORSE:
            morse_code += NESTED_MORSE[char]
        else:
            return AssertionError("the arguments are bad")
    return morse_code


def main():
    """
    Main function that takes a string as a command line argument
        and encodes it into Morse Code.
    """
    if len(sys.argv) != 2:
        print(AssertionError("the arguments are bad"))
        return
    print(morse_encode(sys.argv[1]))


if __name__ == "__main__":
    main()
