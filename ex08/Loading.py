def ft_tqdm(lst):
    """
    A simplified function mimicking the functionality of tqdm.

    This function takes an iterable, iterates through it, and for each iteration,
    calculates the progress as a percentage and prints a progress bar.

    Note: This function doesn't include elapsed time and items per second, unlike tqdm.

    Args:
        lst: The iterable to iterate through.

    Yields:
        Each item of the iterable.

    Prints:
        A progress bar representing the iteration status.
    """

    total = len(lst)
    for i, item in enumerate(lst):
        percent = (i + 1) * 100 / total
        progress_bar = '=' * (i * 100 // total) + '>' + ' ' * ((total - i - 1) * 100 // total)
        print(f'{percent:.2f}% |{progress_bar}| {i+1}/{total}', end='\r')
        yield item
    print()
