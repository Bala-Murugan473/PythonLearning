# If we need to pass the parameter as keyword only in function call, we can use *
# parameters need to pass as keyword argument should place after *

def keyword_only_parameter(*,arg1,arg2):
    print(arg1)
    print(arg2)


keyword_only_parameter(arg1=2,arg2=3)

# If positional argument is passed in the function call, then
# TypeError: method takes 0 positional argument but 1 was given

# All parameter after * is considered as keyword arguments.
