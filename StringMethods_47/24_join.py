print("24. JOIN")
print("*" * 83)
print(
    """1. The calling string will placed inbetween the given strings
2. kind of concatinating method
3. Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'"""
)
print("*" * 79)
print("SYNTAX => String.join(any_Iterable_type )")
print("*" * 79)
calling_string = "**"
print("Calling string =>", calling_string)
strlst = ["ab", "bc", "cd"]
strtup = ("ab", "bc", "cd")
print("Given List type:", strlst)
print("Given Tuple type:", strtup)
print("ans :", calling_string.join(strlst))  # ab**bc**cd
print("ans :", calling_string.join(strtup))
print(" ".join(strtup))

print("*" * 79 + "\n\n****** BUILT IN DOC ******")
help(str.join)

# \t is an escape sequence to use TAB
# \n is an escape sequence to use ENTER
