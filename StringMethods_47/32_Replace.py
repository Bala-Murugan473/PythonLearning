print("32. REPLACE")
print("*" * 83)
print(
    """1. Replace old substring with new substring
2. By default, it replace all the matching occurrences
3. Returns new string"""
)
print("*" * 83)
print(
    """SYNTAX => String.replace(old,new,count)
default count = -1, means replace all"""
)
print("*" * 83)

nm = "python*python*python"
print("Given String =>", nm)
print('str.replace("python", "king") =>', nm.replace("python", "king"))
print('str.replace("python", "king", 1) =>', nm.replace("python", "king", 1))

print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.replace)

# \n is an escape sequence to use ENTER
