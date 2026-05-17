"""Solution for Stepik course solutions: Generation Py / Professional / Chapter 3 / Part 3 1 / Step 20."""

from datetime import date
from typing import List, Tuple


def get_min_max(dates: List[date]) -> Tuple[date, date]:
    if not dates:
        return ()
    return (min(dates), max(dates))
