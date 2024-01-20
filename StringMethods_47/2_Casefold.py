print("2. CASEFOLD\n" + "*" * 83)

print(
    """1. Return a version of the string suitable for caseless comparisons
2. Similar to lower(), but more aggressive(effective)
3. Returns new string, doesn't change the original string"""
)

print("*" * 83)
print("""SYNTAX => String.casefold()""")
print("*" * 83)

name = "Basic Python"

casefolded_name = name.casefold()

print(name, "- casefold() => ", casefolded_name)
print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.casefold)

print("*" * 83)
print("ref CasefoldVsLower.py for comparison (casefold() - lower())\n")
# \n is an escape sequence to use ENTER
