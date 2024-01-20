print("1. CAPITALIZE\n" + "*" * 83)

print(
    """1. Make the first character upper case and the rest all lowercase
2. Capitalize() method is used to capitalize the first letter of a string
3. Returns new string, doesn't change the original string"""
)

print("*" * 83)
print("""SYNTAX => String.capitalize()""")
print("*" * 83)

name = "python"
name1 = "basic python"
name2 = "bAsic PYthon"
name3 = "bAsic PYTHON t"

cap = name.capitalize()
cap1 = name1.capitalize()
cap2 = name2.capitalize()
cap3 = name3.capitalize()

print("Given string :", name, " \t\t=> Capitalized string :", cap)
print("Given string :", name1, " \t\t=> Capitalized string :", cap1)
print("Given string :", name2, " \t\t=> Capitalized string :", cap2)
print("Given string :", name3, " \t=> Capitalized string :", cap3)

print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.capitalize)

# \t is an escape sequence to use TAB
# \n is an escape sequence to use ENTER
