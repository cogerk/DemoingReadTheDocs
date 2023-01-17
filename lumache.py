"""
Lumache - Python library for cooks and food lovers.
"""

__version__ = "0.1.0"


def random_list(n):
    """Return a list of random numbers

    This is basically randint

    Args:
        n (int): The number of random numbers to return

    Returns:
        list: The list of random numbers

    Examples:
        Apparently you need to use the (doctest)[https://docs.python.org/3/library/doctest.html]

        >>> random_list(4)
        [4, 7, 2, 1]

    """
    return [4 for i in n]
