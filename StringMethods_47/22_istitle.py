print("22. ISTITLE")
print("*" * 83)
print(
    """1. Returns true if first letter of each word is uppercase
2. Used to check weather the string follows the title condition"""
)
print("*" * 83)
print("SYNTAX => String.istitle()")
print("*" * 83)

name = "bala"
nam1 = "Bala murugan"
nam2 = "Bala Murugan"
print(name, name.istitle(), sep=" is title? = ")
print(nam1, nam1.istitle(), sep=" is title? = ")
print(nam2, nam2.istitle(), sep=" is title? = ")


print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.istitle)

# \n is an escape sequence to use ENTER
