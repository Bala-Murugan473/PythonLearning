print("8. FIND")
# ref 11_Index.py , 33_Rfind.py, 34_Rindex
print("*" * 83)
print(
    """1. Returns first index of the substring present in the given string
2. If the given substring is not present it returns -1
3. Can also check with slicing the string as well
4. Same like index but doesn't throws error if the substring is not found
5. Case sensitive
6. Returns Integer"""
)
print("*" * 83)
print(
    """SYNTAX => String.find(substring,start_index,end_index)
start_index and end_index are optional"""
)
print("*" * 83)

txt = "Basic python"

index1 = txt.find("c")
index2 = txt.find("z")  # 'z' is not present
index3 = txt.find("")  # when passing empy string it will returns 0

print("Given String <=", txt)
print("'c' is at index =>", index1)
print("'z' is at index =>", index2)
print("'' is at index =>", index3)


print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.find)

# \n is an escape sequence to use ENTER
