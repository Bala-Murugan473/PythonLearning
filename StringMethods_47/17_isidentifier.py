print("17. ISIDENTIFIER")
# ref keyword and identifier.txt
print("*" * 83)
print(
    """1. Return True if the string is a valid Python identifier
2. Can be used to check weather the given string is a python identifier
3. Return False for '1method' since numeric prefix aren't allowed as identifier
4. Return True for 'method' since it follows identifiers rule"""
)
print("*" * 83)
print("SYNTAX => String.isidentifier()")
print("*" * 83)

txt1 = "my_method"
txt2 = "1my_method"
txt3 = "my_method1"

print(txt1, ": isidentifier() =>", txt1.isidentifier())
print(txt2, ": isidentifier() =>", txt2.isidentifier())
print(txt3, ": isidentifier() =>", txt3.isidentifier())


print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.isidentifier)
