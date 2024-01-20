# inverse of lower() method, ref 26_Lower.py
print("*" * 79)
print("1. Converts the given string to uppercase")
print("2. Doesn't change the original string")
print("3. Returns new string")
print("*" * 79)

print("""SYNTAX => String.upper()""")
print("*" * 79)

st = "basic python"
st1 = "Basic Python"
st2 = "baSIC PYthon"
st3 = "BASIC PYTHON"

print(st, "- upper => ", st.upper())
print(st1, "- upper => ", st1.upper())
print(st2, "- upper => ", st2.upper())
print(st3, "- upper => ", st3.upper())

print("*" * 79 + "\n\n****** BUILT IN DOC ******")
help(str.upper)

# \n is an escape sequence to use ENTER
