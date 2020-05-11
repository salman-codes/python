def f(a, b, c):
    """
    >>> f([1, 2, 3], [2, 3], 'b')
    TypeError: can't multiply sequence by non-int of type 'str'

    >>> f(22, 'abc', 2)
    44

    >>> f([77.0, 12], {'a': 'a'}, 1)
    [77.0, 12, {'a': 'a'}]
    """
    if type(a) is list:
        a.append(b)
    return  a * c


if __name__ == "__main__":
    import doctest
    doctest.testmod()