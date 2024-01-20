print("20. PRINTABLE")
print("*" * 83)
print(
    """1. A string is printable if all of its characters are considered\
 printable in repr() or if it is empty
2. String with escape sequences are not printable, since escape sequence is
not a printable characters"""
)
print("*" * 83)
print("SYNTAX => String.isprintable()")
print("*" * 83)

name = "bala123@ ("
name1 = "bala\n123@ ("
name2 = ""
print(name, name.isprintable(), sep=" isprintable? = ")
print(name1, name1.isprintable(), sep=" isprintable? = ")
print("empty string :" + name2, name2.isprintable(), sep=" isprintable? = ")

print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.isprintable)
