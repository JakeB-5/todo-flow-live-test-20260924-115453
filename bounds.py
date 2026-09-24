def clamp(value, lower, upper):
    """Return value limited to the inclusive range [lower, upper].

    Returns lower if value is below the range, upper if value is above the
    range, and value itself otherwise. Raises ValueError if lower > upper.
    """
    if lower > upper:
        raise ValueError(
            "lower bound {!r} is greater than upper bound {!r}".format(lower, upper)
        )
    if value < lower:
        return lower
    if value > upper:
        return upper
    return value
