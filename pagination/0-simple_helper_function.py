#!/usr/bin/env python3
""" Simple pagination tool """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns start and end index for a given page and page size.
    Used to slice datasets for pagination.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
