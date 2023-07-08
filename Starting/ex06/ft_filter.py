def ft_filter(function, iterable):
    """
    ft_filter(function, iterable) -> list

    Return a list of items in iterable for which function(item) is true.
    If function is None, return the items that are true.
        numbers = [1, 2, 3, 4, 5, 6]
        evens = list(filter(lambda n: n % 2 == 0, numbers))
        [2, 4, 6]
    """
    if function is None:
        return [item for item in iterable if item]
    else:
        return [item for item in iterable if function(item)]
