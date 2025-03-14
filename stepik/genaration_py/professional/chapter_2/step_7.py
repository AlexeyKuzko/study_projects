def is_valid(string):
    return len(string) in {4, 5, 6} and all(c in "0123456789" for c in string)
