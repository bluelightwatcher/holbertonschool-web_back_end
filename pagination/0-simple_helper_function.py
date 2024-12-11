#!/usr/bin/env python3
"""
Module that contains the helper function `index_range`.
This function is used to calculate the start and end indexes for pagination.
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Calculate the range of indexes for the given page and page size.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple[int, int]: A tuple containing the start index (inclusive) and
                         the end index (exclusive) for the given page.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
