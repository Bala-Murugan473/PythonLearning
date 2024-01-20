print("34. RFIND")
# ref 8_Find.py , 11_Index.py
print("*" * 79)
print(
    """1. Same as 'find' method, but starts finding index from right
2. If the given substring is not present it returns -1
3. Can also check by slicing the string as well
4. Doesn't throw error
3. Returns Integer"""
)
print("*" * 79)
print(
    """SYNTAX => String.rfind("substring",startindex, endindex)
Start and End indices are optional parameters, behave same as slicing"""
)
print("*" * 79)

help(str.rfind)

name = "bala murugan"
print("given string : ", name)
substring_index = name.rfind("a")
print("sub string is a index : ", substring_index)
print(name[substring_index:])
