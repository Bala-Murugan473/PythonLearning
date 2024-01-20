print("3. CENTER\n" + "*" * 83)

print(
    """1. Can be used to get a centralized string with given length
2. Padding is done using the specified fill character
3. Default filling character is space
4. Returns a new centered string of length width"""
)
print("*" * 83)
print("""SYNTAX => String.center(width : int, fillchar=' ')""")
print("*" * 83)

name = "Python"
print("Center of size 20 with default char :", name.center(20))
print('Center of size 20 with given"^"char :', name.center(20, "^"))

print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.center)
