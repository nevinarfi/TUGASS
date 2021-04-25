"""
This is a pure Python implementation of the Geometric Series algorithm
https://en.wikipedia.org/wiki/Geometric_series

Run the doctests with the following command:
python3 -m doctest -v geometric_series.py
or
python -m doctest -v geometric_series.py
For manual testing run:
python3 geometric_series.py
"""


def geometric_series(nth_term: int, start_term_a: float, common_ratio_r: float) -> list[float]:
    """Pure Python implementation of Geometric Series algorithm
    :param nth_term: The last term (nth term of Geometric Series)
    :param start_term_a : The first term of Geometric Series
    :param common_ratio_r : The common ratio between all the terms
    :return: The Geometric Series starting from first term a and multiple of common
        ration with first term with increase in power till last term (nth term)
    Examples:
    >>> geometric_series(4, 2, 2)
    [2, 4.0, 8.0, 16.0]
    >>> geometric_series(4.0, 2.0, 2.0)
    [2.0, 4.0, 8.0, 16.0]
    >>> geometric_series(4, 2, -2)
    [2, -4.0, 8.0, -16.0]
    >>> geometric_series(4, -2, 2)
    [-2, -4.0, -8.0, -16.0]
    >>> geometric_series(-4, 2, 2)
    []
    >>> geometric_series(0, 100, 500)
    []
    >>> geometric_series(1, 1, 1)
    [1]
    >>> geometric_series(0, 0, 0)
    []
    """
    series = []
    for power in range(nth_term):
        series.append(start_term_a * pow(common_ratio_r, power))
    return series


if __name__ == "__main__":
    nth_term = int(input("Enter the last number (n term) of the Geometric Series: "))
    start_term_a = int(input("Enter the starting term (a) of the Geometric Series: "))
    common_ratio_r = int(input(
        "Enter the common ratio between two terms (r) of the Geometric Series: "
    ))
    print("Formula of Geometric Series => a + ar + ar^2 ... +ar^n")
    print(geometric_series(nth_term, start_term_a, common_ratio_r))
