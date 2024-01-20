print("38. RSTRIP")
# inverse of lstrip() method, ref 27_Lstrip.py
print("*" * 83)
print(
    """1. Return a copy of the string with trailing whitespace removed.
2. By default it removes the trailing whitespaces
3. If chars is given, then it remove all the chars.
4. The argument is a set of trailing characters that will be removed as many \
\ntimes as they occur
5. In other word if the string endswith passing characters, it removes all of
them from the end
6. Can also used to remove the part of substring from RIGHT """
)
print("*" * 83)
print("""SYNTAX => String.rstrip("characters")""")
print("*" * 83)


name = "basic python "
txt = "python,,,,,,aabbcc..*.."
print(name + ".rstrip() =>", name.rstrip())
print(name + ".rstrip('hon ') =>", name.rstrip("hon "))
print(txt + ".rstrip('.*bc') =>", txt.rstrip(".*bc"))
print(
    "# From the above line we can observe that, rstrip will remove characters\
 \nfrom last if mentioned. It iterate the ending character one by one, if the \
\nending character in mentioned parameter it removes, else it stop"
)

print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.rstrip)
