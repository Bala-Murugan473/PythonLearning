print("15. ISDECIMAL")
print("*" * 83)
print(
    """1. Return True if the string is a decimal string
2. A string is a decimal string if all characters in the string are decimal and
there is at least one character in the string
3. It validates only whole number"""
)
print("*" * 83)
print("SYNTAX => String.isdecimal()")
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

print(txt1, txt1.isdecimal(), sep=" is decimal ? = ")
print(txt2, txt2.isdecimal(), sep=" is decimal ? = ")
print(txt3, txt3.isdecimal(), sep=" is decimal ? = ")
print(txt4, txt4.isdecimal(), sep=" is decimal ? = ")
print(txt5, txt5.isdecimal(), sep=" is decimal ? = ")
print(txt6, txt6.isdecimal(), sep=" is decimal ? = ")


print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.isdecimal)

# \n is an escape sequence to use ENTER
