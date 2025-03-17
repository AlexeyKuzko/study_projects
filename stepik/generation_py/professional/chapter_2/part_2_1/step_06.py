def same_parity(numbers):
    if not numbers:
        return []  # Return an empty list if input is empty
    first_parity = numbers[0] % 2  # Determine parity of the first element
    return [num for num in numbers if num % 2 == first_parity]
