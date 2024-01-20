print("39. SPLIT")
print("*" * 83)
print(
    """1. Split the string with given substring(separator or delimitter)
2. If the separator is not defined, then it split on any whitespace characters
3. The number of splits required can also be define, By default -1 (means all)
4. If max split count specified, splitting starts from left
5. Returns list of strings
"""
)
print("*" * 83)
print("""SYNTAX => String.split("separator",splitCount)
 separtor is optional = default can be any whitespace
 splitCount is optional = default is -1 means all""")
print("*" * 83)


txt = "Basic Python Methods"
print("Given String <=", txt)
print("Default split =>", txt.split())
print("By separator('h') =>", txt.split("h"))
print("By separator('h') & maxsplit(1)=>", txt.split("h", 1))


print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.split)
