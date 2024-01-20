print("18. ISLOWER")
# ref 23_Isupper.py
print("*" * 83)
print("1. Return True if the string is is full of lowercased characters")
print("*" * 83)
print("SYNTAX => String.islower()")
print("*" * 83)

name = "baLa"
name1 = "bala"
name2 = "BALA"
print(name.isupper())
print(name, name.islower(), sep=" = islower? ")
print(name1, name1.islower(), sep=" = islower? ")
print(name2, name2.islower(), sep=" = islower? ")


print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.islower)

# \n is an escape sequence to use ENTER
