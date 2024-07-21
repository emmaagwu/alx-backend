#!/usr/bin/env python3
"""Simple pagination sample.
"""
import csv
from typing import List, Tuple


def index_range(page: int, items_per_page: int) -> Tuple[int, int]:
    """Determines the starting and ending indices for a given
      page and items per page.

    Args:
        page (int): The current page number.
        items_per_page (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the starting and ending indices.
    """
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes a new Server instance.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Loads and caches the dataset from the CSV file if not
          already loaded.

        Returns:
            List[List]: The cached dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Fetches a page of data.

        Args:
            page (int): The current page number.
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of rows corresponding to the page of data.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]
