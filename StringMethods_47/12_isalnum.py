print("12. ISALUM")
print("*" * 83)
print(
    """1. Return True if the string is an alpha-numeric string, False otherwise
2. A string is alpha-numeric if all characters are alpha-numeric and there is
at least 1 character in the string
3. Only a to z,A to Z and 0-9"""
)
print("*" * 83)
print("SYNTAX => String.isalnum()")
print("*" * 83)

num = "123"
text = "bala"
numtext = "123bala"
num_text = "123 bala"
numsymbol = "123@"
print(num, num.isalnum(), sep=" = isalum? ")
print(text, text.isalnum(), sep=" = isalum? ")
print(numtext, numtext.isalnum(), sep=" = isalum? ")
print(num_text, num_text.isalnum(), sep=" = isalum? ")
print(numsymbol, numsymbol.isalnum(), sep=" = isalum? ")

print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.isalnum)

# \n is an escape sequence to use ENTER
