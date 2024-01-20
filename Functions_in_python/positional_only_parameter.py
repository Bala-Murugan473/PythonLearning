# if we want the parameter to pass as positional only means we can use the forward slash
# as an optional parameter in the function definition

# The parameter which need to pass as positional only need to place before the forward slash

# If a keyword argument is passed in the given positional parameter method, it will throw
# TypeError: method got some positional-only arguments passed as keyword

# All parameter before forward slash is consider as positional parameters.
# Positional parameters should come first in the function call

def positional_only_parameter(arg1, arg2, /):
    print(arg1)
    print(arg2)


positional_only_parameter(1, 2)
