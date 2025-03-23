from datetime import date, timedelta


def saturdays_between_two_dates(start: date, end: date) -> int:
    if start > end:
        start, end = end, start

    current_date = start
    saturday_count = 0
    while current_date <= end:
        if current_date.weekday() == 5:  # 5 corresponds to Saturday
            saturday_count += 1
        current_date += timedelta(days=1)

    return saturday_count
