# The argument can have a default value, if the value for that argument is not passed
# then the value in default will take into account.

def default_argument_fn(argument1,argument2=20):
    print(argument1 + argument2)

default_argument_fn(10,10)
default_argument_fn(10)

# !!! The default values are evaluated at the point of function definition in the defining scope.

i = 5
# at the time of function definition,the value for i is 5, which will be the default parameter value
def function_def(arg = i):
    print(arg)

i = 6
# even the value for 'i' is changed from 5 to 6, the below method calling will print 5
function_def(i)

# the default values are evaluated once, except mutable objects like list, dictionary or any other instance

def mutable_default_function(a,lst=[]):
    lst.append(a)
    return lst

print(mutable_default_function(1))
print(mutable_default_function(2))
