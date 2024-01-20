print("37. RSPLIT")
# inverse of split(), ref 39_Split.py
print("*" * 83)
print(
    """1. Split the string with given substring(separator or delimitter)
2. If the separator is not defined, then it split on any whitespace characters
3. The number of splits required can also be define, By default -1 (means all)
4. If max split count specified, splitting starts from right and returns in
 left to right order
5. Returns list of strings
"""
)
print("*" * 83)
print("""SYNTAX => String.rsplit("separator",splitCount)
 separtor is optional = default can be any whitespace
 splitCount is optional = default is -1 means all""")
print("*" * 83)


txt = "Basic Python Methods"
print("Given String <=", txt)
print("Default rsplit =>", txt.rsplit())
print("By separator('h') =>", txt.rsplit("h"))
print("By separator('h') & maxsplit(1)=>", txt.rsplit("h", 1))


print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.rsplit)
