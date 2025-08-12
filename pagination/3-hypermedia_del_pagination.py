#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a page of the dataset starting at a specific index
        with hypermedia pagination metadata.

        Args:
        index (int): The starting index of the dataset page (0-indexed).
        page_size (int): The number of items to include in the page.

        Returns:
        Dict: A dictionary containing:
            - index (int): The current start index of the page.
            - next_index (int): The starting index of the next page.
            - page_size (int): The number of items requested for the page.
            - data (List[List]): The list of dataset rows for the current page.
        """
        assert 0 <= index
        dataset = self.dataset()
        data = dataset[index:index + page_size]
        return {
            "index": index,
            "next_index": index + 1,
            "page_size": page_size,
            "data": data
        }
    