print("41. STARTSWITH")
# inverse of endswith() method ref 6_Endswith.py
print("*" * 79)
print(
    """1. Used to validate string is starting with given substring or tuple of\
 strings
2. Can also check by slicing the string as well
3. Returns bool"""
)
print("*" * 79)
print(
    """SYNTAX => String.startswith("substring",startindex, endindex)
Start and End indices are optional parameters, behave same as slicing"""
)
print("*" * 79)

st = "Basic Python"

b1 = st.startswith("Ba")
b2 = st.startswith("ba")  # Case sensitive
b3 = st.startswith("Py")
b4 = st.startswith(("Ca", "Ba"))  # True, if any one item satisfice
b5 = st.startswith("c ", 4)  # Sliced string
# note 'space' is also a charater,  'c ' is a substring wth two characters

"""b1,b2,b3,b4,b5 are all bool type"""

print(st, "- startswith : Ba =>", b1)
print(st, "- startswith : ba =>", b2)
print(st, "- startswith : Py =>", b3)
print(st, "- startswith : Ca or Ba =>", b4)
print(st[4:], "- startswith : 'c ' =>", b5)

print("*" * 79 + "\n\n****** BUILT IN DOC ******")
help(str.startswith)

# \t is an escape sequence to use TAB
# \n is an escape sequence to use ENTER
