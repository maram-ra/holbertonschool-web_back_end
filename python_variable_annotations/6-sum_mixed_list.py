#!/usr/bin/env python3
"""Function that sums a mixed list of integers and floats, returns the total as a float."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list containing ints and floats as a float."""
    return sum(mxd_lst)
