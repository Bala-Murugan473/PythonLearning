print("19. ISDECIMAL")
print("*" * 83)
print(
    """1. Return True if the string is a numeric string
2. A string is a numeric string if all characters in the string are numeric and
there is at least one character in the string
3. Mainly used to check weather the string is numeral(Roman,Japanese,Tamil)
3. It validates numerals, whole number, fraction and exponentials
5. If a string is numeric then it must be digit and decimal also"""
)
print("*" * 83)
print("SYNTAX => String.isnumeric()")
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

print(txt1, txt1.isnumeric(), sep=" is numeric ? = ")
print(txt2, txt2.isnumeric(), sep=" is numeric ? = ")
print(txt3, txt3.isnumeric(), sep=" is numeric ? = ")
print(txt4, txt4.isnumeric(), sep=" is numeric ? = ")
print(txt5, txt5.isnumeric(), sep=" is numeric ? = ")
print(txt6, txt6.isnumeric(), sep=" is numeric ? = ")


print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.isnumeric)

# \n is an escape sequence to use ENTER
