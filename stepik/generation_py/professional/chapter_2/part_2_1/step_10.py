"""Solution for Stepik course solutions: Generation Py / Professional / Chapter 2 / Part 2 1 / Step 10."""


def filter_anagrams(word: str, words: list) -> list:
    sorted_word = sorted(word)
    return [w for w in words if sorted(w) == sorted_word]
