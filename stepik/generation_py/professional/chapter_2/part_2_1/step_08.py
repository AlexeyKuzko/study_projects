"""Solution for Stepik course solutions: Generation Py / Professional / Chapter 2 / Part 2 1 / Step 08."""


def print_given(*args, **kwargs):
    for arg in args:
        print(arg, type(arg))

    for key in sorted(kwargs):
        print(key, kwargs[key], type(kwargs[key]))
