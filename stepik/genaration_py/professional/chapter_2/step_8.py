def print_given(*args, **kwargs):
    for arg in args:
        print(arg, type(arg))

    for key in sorted(kwargs):
        print(key, kwargs[key], type(kwargs[key]))