while True:
    try:
        line = input()
        print(line[::-1])
    except EOFError:
        break
