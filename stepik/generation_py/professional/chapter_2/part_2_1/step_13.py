"""Solution for Stepik course solutions: Generation Py / Professional / Chapter 2 / Part 2 1 / Step 13."""


def spell(*words):
    result = {}
    for word in words:
        first_letter = word[0].lower()
        word_length = len(word)
        if first_letter not in result or word_length > result[first_letter]:
            result[first_letter] = word_length
    return result
