"""Solution for Stepik course solutions: Generation Py / Professional / Chapter 4 / Part 4 1 / Step 11."""

from datetime import datetime

dates = []
try:
    while True:
        date_str = input().strip()
        date = datetime.strptime(date_str, "%Y-%m-%d")
        dates.append(date)
except EOFError:
    pass

if dates:
    min_date = min(dates)
    max_date = max(dates)
    diff = max_date - min_date
    print(diff.days)
