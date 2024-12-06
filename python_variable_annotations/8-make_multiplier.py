#!/usr/bin/env python3
"""
This module contains the make_multiplier function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier to use.

    Returns:
        Callable[[float], float]: A multiplying function.
    """
    def multiplier_function(x: float) -> float:
        """
        Multiplies a float by the outer multiplier.

        Args:
            x (float): The number to multiply.

        Returns:
            float: The result of the multiplication.
        """
        return x * multiplier

    return multiplier_function
