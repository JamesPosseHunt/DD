from random import randint

def roll_die(sides: int) -> int:
    """
    Simulate rolling a die with a specified number of sides.
    
    Args:
        sides (int): Number of sides on the die (e.g., 6 for a d6).
    
    Returns:
        int: A random number between 1 and `sides` inclusive.
    
    Raises:
        ValueError: If `sides` is less than 1.
    """
    if sides < 1:
        raise ValueError("Die must have at least one side.")
    return randint(1, sides)
