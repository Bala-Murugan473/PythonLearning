print("42. STRIP")
# Combination of rstrip() & lstrip() methods, ref 27_Lstrip.py &37_Rstrip.py
print("*" * 83)
print(
    """1. Return a copy of the string with leading and trailing whitespace\
 removed.
2. By default it removes the whitespaces
3. If chars is given, then it remove all the chars.
4. The argument is a set of characters that will be removed as many \
\ntimes as they occur
5. In otherword,if the string start or end with passing characters, it removes
all of them from the start or end"""
)
print("*" * 83)
print("""SYNTAX => String.strip("set_of_characters")""")
print("*" * 83)

txt = "  Basic python Basic  "
print("Given String =>", txt)
print("Strip() =>", txt.strip())
print("Strip('abciB ') =>", txt.strip("abciB "))


print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.strip)
