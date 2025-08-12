#!/usr/bin/env python3
"""Module providing hypermedia pagination over a CSV dataset."""
import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns start and end index for a given page and page size.
    Used to slice datasets for pagination.
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
            # Skip header row
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """
        Return a specific page of the dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Return hypermedia-style pagination metadata along with the page data.

        Keys:
            - page_size: length of the returned page (may be 0 if out of range)
            - page: current page number
            - data: the dataset page (same as get_page output)
            - next_page: next page number or None
            - prev_page: previous page number or None
            - total_pages: total number of pages (ceil)
        """
        # Reuse get_page as required
        data_page = self.get_page(page, page_size)
        actual_size = len(data_page)

        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size) if page_size else 0

        # Compute next_page
        # next exists only if there are more items after current window
        next_page = page + 1 if (page * page_size) < total_items else None

        # prev_page exists if page > 1 (even if current page is empty)
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": actual_size,
            "page": page,
            "data": data_page,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
