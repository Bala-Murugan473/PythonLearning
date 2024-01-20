print("14. ISASCII")
print("*" * 83)
print(
    """1. Return True if all characters in the string are ASCII
2. Empty string is ASCII too. """
)
print("*" * 83)
print("SYNTAX => String.isascii()")
print("*" * 83)


asc = "123abc*& ([-])"
print(asc, asc.isascii(), sep=" is ascii ? = ")

print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.isascii)

# \n is an escape sequence to use ENTER
