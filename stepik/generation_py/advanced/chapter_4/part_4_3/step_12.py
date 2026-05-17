"""Solution for Stepik course solutions: Generation Py / Advanced / Chapter 4 / Part 4 3 / Step 12."""


def pack_duplicates(s):
    s = s.split()
    result = []
    current = [s[0]]
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current.append(s[i])
        else:
            result.append(current)
            current = [s[i]]
    result.append(current)
    return result


s = input()
print(pack_duplicates(s))
