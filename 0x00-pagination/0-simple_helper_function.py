#!/usr/bin/env python3
"""a funct that returns the start and end index"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a range of indexes"""
    start = (page - 1) * page_size
    end = start + page_size
    return start, end
