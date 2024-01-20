print("6. ENDSWITH")
# inverse of startswith() method ref 41_Startswith.py
print("*" * 83)
print(
    """1. Used to validate the string is ending with given substring or\
 tuple of strings
2. Can also check by slicing the string as well
3. Returns bool"""
)
print("*" * 83)
print(
    """SYNTAX => String.endswith("substring",startindex, endindex)
Start and End indices are optional parameters, behave same as slicing"""
)
print("*" * 83)

st = "Basic Python"

b1 = st.endswith("on")
b2 = st.endswith("ON")  # Case sensitive
b3 = st.endswith("ic")
b4 = st.endswith(("on", "an"))  # True, if any one item satisfice
b5 = st.endswith("Py", 0, 8)  # Sliced sting

"""b1,b2,b3,b4,b5 are all bool type"""

print(st, "- endswith : on =>", b1)
print(st, "- endswith : ON =>", b2)
print(st, "- endswith : ic =>", b3)
print(st, "- endswith : on or an =>", b4)
print(st[0:8], "- endswith : Py =>", b5)

print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.endswith)

# \t is an escape sequence to use TAB
# \n is an escape sequence to use ENTER
