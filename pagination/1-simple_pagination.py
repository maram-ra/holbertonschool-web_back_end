#!/usr/bin/env python3
"""Module providing simple pagination over a CSV dataset."""
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns start and end index for a given page and page size.
    Used to slice datasets for pagination (Python slice is [start:end)).
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List[str]]:
        """Return the cached dataset (header skipped)."""
        if self.__dataset is None:
            with open(self.DATA_FILE, encoding="utf-8") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header row
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """
        Return a specific page of the dataset.

        Args:
            page (int): 1-indexed page number (must be > 0).
            page_size (int): number of items per page (must be > 0).

        Returns:
            List[List[str]]: The sliced page of the dataset.
        """
        # Input validation as required
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()
        return data[start:end]
