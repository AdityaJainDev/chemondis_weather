# Used to store utility functions for the weather app.


def deg_to_direction(degrees):
    val = int((degrees / 22.5) + 0.5)
    directions = [
        "North",
        "North-Northeast",
        "Northeast",
        "East-Northeast",
        "East",
        "East-Southeast",
        "Southeast",
        "South-Southeast",
        "South",
        "South-Southwest",
        "Southwest",
        "West-Southwest",
        "West",
        "West-Northwest",
        "Northwest",
        "North-Northwest",
    ]
    return directions[(val % 16)]
