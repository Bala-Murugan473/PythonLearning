print("31. REMOVESUFFIX")
# ref 30_removesuffix.py
print("*" * 83)
print(
    """1. Return a str with the given suffix string removed if present
2. Not like rstrip(), where the argument is the set of chars
3. removesuffix will search for exact one match"""
)
print("*" * 83)
print("SYNTAX => String.removeprefix(substring)")
print("*" * 83)

help(str.removesuffix)

name = "bala murugan "
name1 = "balabala murugan"
print(name.removesuffix("gn"))
print(name1.removesuffix("an"))

word = "hubbubbubboo"
print(word.removesuffix("o"))

print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.removesuffix)

# \n is an escape sequence to use ENTER
