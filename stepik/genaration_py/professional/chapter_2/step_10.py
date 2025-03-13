def filter_anagrams(word: str, words: list) -> list:
    sorted_word = sorted(word)
    return [w for w in words if sorted(w) == sorted_word]
