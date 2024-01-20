# A function can be called with arbitrary or variable number of arguments.
# These arguments will be wrapped in the form of tuple
# Any number of normal parameters can be pass before this arbitrary argument,
# but only keyword arguments should pass after the arbitrary argument,
# else it will wrap them together with arbitrary parameter

def arbitrary_arguments_fn(*args):
    s = 0
    for x in args:
        s += x

    print(s)
    print(type(args))


arbitrary_arguments_fn(1, 2, 3, 4, 5)


# An argument prefixed with a single asterisk * for arbitrary positional arguments.
# An argument prefixed with two asterisks ** for arbitrary keyword arguments.
