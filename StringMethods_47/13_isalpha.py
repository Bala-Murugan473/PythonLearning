print("13. ISALPHA")
print("*" * 83)
print(
    """1. Return True if the string is an alpha-numeric string, False otherwise
2. Only a to z,A to Z and 0-9"""
)
print("*" * 83)
print("SYNTAX => String.isalpha()")
print("*" * 83)

num = "123"
text = "bala"
numtext = "123bala"
num_text = "123 bala"
numsymbol = "123@"

print(num, num.isalpha(), sep=" = isalpha? ")
print(text, text.isalpha(), sep=" = isalpha? ")
print(numtext, numtext.isalpha(), sep=" = isalpha? ")
print(num_text, num_text.isalpha(), sep=" = isalpha? ")
print(numsymbol, numsymbol.isalpha(), sep=" = isalpha? ")

print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.isalpha)

# \n is an escape sequence to use ENTER
