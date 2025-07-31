#!/usr/bin/env python3
"""Annotate parameters and return value using duck typing."""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return list of tuples with elements and their lengths."""
    return [(i, len(i)) for i in lst]
