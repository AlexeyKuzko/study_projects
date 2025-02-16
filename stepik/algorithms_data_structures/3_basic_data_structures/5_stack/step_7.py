def is_correct(s):
    stack = []
    mapping = {")": "(", "]": "[", "}": "{"}
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        elif char in mapping.values():
            stack.append(char)
    return not stack


s = input()
if is_correct(s):
    print("yes")
else:
    print("no")
