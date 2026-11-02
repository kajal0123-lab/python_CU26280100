t = (1, 2, 3, 2, 4, 1, 5, 3)

repeated = tuple(
    x for i, x in enumerate(t)
    if x in t[:i] and x not in t[:i-1]
)