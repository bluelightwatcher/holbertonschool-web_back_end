#!/usr/bin/env python3
"""
Module that provides a function to compute the sum of a list of floats.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Computes the sum of a list of floats.

    Args:
        input_list (List[float]): A list of floats.

    Returns:
        float: The sum of the floats in the list.
    """
    return sum(input_list)
