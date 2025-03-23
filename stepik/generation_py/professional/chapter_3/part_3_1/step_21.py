from datetime import date, timedelta
from typing import List


def get_date_range(start: date, end: date) -> List[date]:
    if start > end:
        return []
    delta = timedelta(days=1)
    current_date = start
    date_list = []
    while current_date <= end:
        date_list.append(current_date)
        current_date += delta
    return date_list
