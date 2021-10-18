from __future__ import annotations


def check_polygon(nums: list[float]) -> bool:
    """
    Takes list of possible side lengths and determines whether a
    two-dimensional polygon with such side lengths can exist.

    Returns a boolean value for the < comparison
    of the largest side length with sum of the rest.
    Wiki: https://en.wikipedia.org/wiki/Triangle_inequality

    >>> check_polygon([6, 10, 5])
    True
    >>> check_polygon([3, 7, 13, 2])
    False
    >>> check_polygon([1, 4.3, 5.2, 12.2])
    False
    >>> nums = [3, 7, 13, 2];check_polygon(nums); nums
    False
    [3, 7, 13, 2]
    >>> check_polygon([])
    Traceback (most recent call last):
        ...
    ValueError: List is invalid
    """
    if not nums:
        raise ValueError("List is invalid")
    copy_nums = nums.copy()
    copy_nums.sort()
    return copy_nums[-1] < sum(copy_nums[:-1])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
