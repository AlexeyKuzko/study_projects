from datetime import date
from typing import List, Tuple


def get_min_max(dates: List[date]) -> Tuple[date, date]:
    if not dates:
        return ()
    return (min(dates), max(dates))
