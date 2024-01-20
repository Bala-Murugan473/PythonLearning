print("11. INDEX")
# ref 8_Find.py , 33_Rfind.py , 34_Rindex
print("*" * 83)
print(
    """1. Returns first index of substring present in the given substring
2. Raises ValueError when the substring is not found
3. Can also check with slicing the string as well
4. Same like find but throws value error if the substring is not found
5. Case sensitive
6. Returns Integer"""
)
print("*" * 83)
print(
    """SYNTAX => String.index(substring,start_index,end_index)
start_index and end_index are optional"""
)
print("*" * 83)

txt = "Basic python"

index1 = txt.index("c")
# index2= txt.index('z')   # 'z' is not present, will throws ValueError
index3 = txt.index("")  # when passing empy string it will returns 0

print("Given String <=", txt)
print("'c' is at index =>", index1)
# print("'z' is at index =>",index2)
print("'' is at index =>", index3)

print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.index)

# \n is an escape sequence to use ENTER
