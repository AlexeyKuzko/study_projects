def convert(string: str) -> str:
    lower_count = sum(1 for char in string if char.islower())
    upper_count = sum(1 for char in string if char.isupper())

    if lower_count >= upper_count:
        return string.lower()
    else:
        return string.upper()
