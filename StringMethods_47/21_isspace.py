print("21. ISSPACE")
print("*" * 83)
print("1. Return True if all the characters in the string is whitespace")
print("*" * 83)
print("SYNTAX => String.isspace()")
print("*" * 83)

a = "     "
b = ""
c = " avc"
print('"' + a + '"', a.isspace(), sep=" isspace? = ")
print('"' + b + '"', b.isspace(), sep=" isspace? = ")
print('"' + c + '"', c.isspace(), sep=" isspace? = ")


print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.isspace)
