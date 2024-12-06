#!/usr/bin/env python3
"""
Module that provides a function to compute the sum of a list of int or floats.
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Computes the sum of a list of floats.

    Args:
        mxd_list (List[int | float]): A list of int or floats.

    Returns:
        float: The sum of the elements in the list.
    """
    return sum(mxd_list)
