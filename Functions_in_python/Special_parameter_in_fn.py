# '/' and '*' are optional parameters in a function definition.
# These symbol indicates how the parameter can be pass when calling the function.
# Generally we can pass parameter in function by positional or keyword or both.

# If / or * not present in a function, arguments can be passed by positional or keyword or both.

# arguments before / are positional
# arguments after * are keyword
# arguments in between / and * can be pass as keyword or positional

def positional_only_parameter(arg1, arg2, /):
    print(arg1)
    print(arg2)


positional_only_parameter(1, 2)


def keyword_only_parameter(*,arg1,arg2):
    print(arg1)
    print(arg2)


keyword_only_parameter(arg1=2,arg2=3)

def positional_or_keyword(arg1, arg2, /,arg3,arg4,*,arg5,arg6):
    # Here arg3 and arg4 can be call as both positional or keyword
    print(arg1,arg2,arg3,arg4,arg5,arg6)