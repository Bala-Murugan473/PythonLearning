print("34. INDEX")
# ref 8_Find.py , 33_Rfind.py
print("*" * 83)
print(
    """1. Returns first index of substring present in the given substring
2. Raises ValueError when the substring is not found
3. Can also check with slicing the string as well
4. Same like index() but start finding from right
5. Case sensitive
6. Returns Integer"""
)
print("*" * 83)
print(
    """SYNTAX => String.rindex(substring,start_index,end_index)
start_index and end_index are optional"""
)
print("*" * 83)

txt = "Basic python c"

index1 = txt.rindex("c")
# index2= txt.index('z')   # 'z' is not present, will throws ValueError
index3 = txt.rindex("")  # when passing empy string it will returns 0

print("Given String <=", txt)
print("'c' is at index =>", index1)
# print("'z' is at index =>",index2)
print("'' is at index =>", index3)

print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.rindex)

# \n is an escape sequence to use ENTER
