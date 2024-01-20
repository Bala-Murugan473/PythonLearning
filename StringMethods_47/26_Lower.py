print("26. LOWER")
# inverse of lower() method, ref 46_Upper.py
print("*" * 83)
print("1. Converts the given string to lowercase")
print("2. Doesn't change the original string")
print("3. Returns new string")
print("*" * 83)

print("""SYNTAX => String.lower()""")
print("*" * 83)

st = "basic python"
st1 = "Basic Python"
st2 = "baSIC PYthon"
st3 = "BASIC PYTHON"

print(st, "- lower => ", st.lower())
print(st1, "- lower => ", st1.lower())
print(st2, "- lower => ", st2.lower())
print(st3, "- lower => ", st3.lower())

print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.lower)

# \n is an escape sequence to use ENTER
