def score(x, y):
    """Calculate the points scored in a single toss of a Darts game."""
    distance_squared = x**2 + y**2

    if distance_squared <= 1**2:
        return 10
    if distance_squared <= 5**2:
        return 5
    if distance_squared <= 10**2:
        return 1
    return 0
