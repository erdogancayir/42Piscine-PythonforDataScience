import sys


def filter_words(string, n):
    """
    filter_words(string, n) -> list

    Return a list of words from the input string that
        have a length greater than n.
        Words are separated by space characters.
    """
    return [word for word in string.split() if len(word) > n]


def main():
    """
    Main function that filters words from the input string
    based on their length.

    Usage: python3 script_name.py "input_string" length
    """
    try:
        assert len(sys.argv) == 3
        S = sys.argv[1]
        assert isinstance(S, str)
        N = int(sys.argv[2])
        print(filter_words(S, N))
    except AssertionError:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
