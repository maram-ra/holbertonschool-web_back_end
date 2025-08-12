#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Optional


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset: Optional[Dict[int, List[str]]] = None

    def dataset(self) -> List[List[str]]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, encoding="utf-8") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            # drop header
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List[str]]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            data = self.dataset()
            # نُفهرس كل الصفوف (يتطابق مع مخرجات المثال)
            self.__indexed_dataset = {i: row for i, row in enumerate(data)}
        return self.__indexed_dataset

    def get_hyper_index(self, index: Optional[int] = None,
                        page_size: int = 10) -> Dict:
        """Deletion-resilient hypermedia pagination

        Returns:
            Dict with keys:
              - index: requested start index (even if missing after deletions)
              - next_index: first valid index after the returned page, or None
              - page_size: actual number of items returned
              - data: list of rows for this page (skipping deleted holes)
        """
        idx = self.indexed_dataset()

        # Defaults and validation
        if index is None:
            index = 0
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0
        # must be within range of the indexed keys
        max_key = max(idx.keys()) if idx else -1
        assert index <= max_key, "index out of range"

        data: List[List[str]] = []
        pos = index

        # Collect up to page_size existing rows, skipping missing keys
        while len(data) < page_size and pos <= max_key:
            row = idx.get(pos)
            if row is not None:
                data.append(row)
            pos += 1

        # Determine next_index: first existing key at/after current cursor
        next_index: Optional[int] = None
        while pos <= max_key:
            if idx.get(pos) is not None:
                next_index = pos
                break
            pos += 1

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index,
        }
