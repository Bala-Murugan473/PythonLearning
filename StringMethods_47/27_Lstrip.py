print("27. LSTRIP")
# inverse of rstrip() method, ref 38_Rstrip.py
print("*" * 83)
print(
    """1. Return a copy of the string with leading whitespace removed.
2. By default it removes the leading whitespaces
3. If chars is given, then it remove all the chars.
4. The argument is a set of leading characters that will be removed as many \
\ntimes as they occur
5. In other word if the string startswith passing characters, it removes all of
them from the end
6. Can also used to remove the part of substring from LEFT"""
)
print("*" * 83)
print("""SYNTAX => String.rstrip("set_of_characters")""")
print("*" * 83)

name = "  Basic python"
print(name.lstrip())
print(name.lstrip("abciB "))

word = "hubbubbubboo"
print(word.lstrip("hub"))
print(
    "returns 'oo' since all the preceding chars are mentioned in the \
argument"
)

print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.lstrip)
