print("23. ISUPPER")
# ref 19_Islower.py
print("*" * 83)
print("1. Return True if the string is is full of uppercased characters")
print("*" * 83)
print("SYNTAX => String.isupper()")
print("*" * 83)

name = "baLa"
name1 = "bala"
name2 = "BALA"
print(name.isupper())
print(name, name.isupper(), sep=" = isupper? ")
print(name1, name1.isupper(), sep=" = isupper? ")
print(name2, name2.isupper(), sep=" = isupper? ")

print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.isupper)
