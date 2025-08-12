# Pagination

## Description
This project shows how to implement pagination in Python.

## Learning Objectives
- Paginate a dataset using `page` and `page_size`.
- Paginate with hypermedia metadata.
- Paginate in a deletion-resilient way.

## Requirements
- Ubuntu 20.04 LTS
- Python 3.9
- Follow pycodestyle (version 2.5.*)
- All functions must have docstrings and type hints

## Files
- 0-simple_helper_function.py
- 1-simple_pagination.py
- 2-hypermedia_pagination.py
- 3-hypermedia_del_pagination.py
- Popular_Baby_Names.csv

## Example
```python
from 0-simple_helper_function import index_range

print(index_range(1, 7))   # (0, 7)
print(index_range(3, 15))  # (30, 45)
