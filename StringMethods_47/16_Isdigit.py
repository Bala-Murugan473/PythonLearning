print("16. ISDIGIT")
print("*" * 83)
print(
    """1. Return True if the string is a digit string
2. A string is a digit string if all characters in the string are digit and
there is at least one character in the string
3. It validates whole number, fraction and exponentials not numerals
4. If a string is digit then it must be decimal also"""
)
print("*" * 83)
print("SYNTAX => String.isdigit()")
print("*" * 83)


txt1 = "123abc*& ([-])"
# decimal
txt2 = "28"
# decimal (dot) is not a string
txt3 = "20.05"
# unicode for 0
txt4 = "\u0030"
# exponential
txt5 = "2²"
# txt5="⅔"
# numeral
txt6 = "\u2167"  # roman eight

print(txt1, txt1.isdigit(), sep=" is digit ? = ")
print(txt2, txt2.isdigit(), sep=" is digit ? = ")
print(txt3, txt3.isdigit(), sep=" is digit ? = ")
print(txt4, txt4.isdigit(), sep=" is digit ? = ")
print(txt5, txt5.isdigit(), sep=" is digit ? = ")
print(txt6, txt6.isdigit(), sep=" is digit ? = ")


print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.isdigit)

# \n is an escape sequence to use ENTER
