print("30. REMOVEPREFIX")
# ref 31_removesuffix.py
print("*" * 83)
print("""1. Return a str with the given prefix string removed if present
2. Not like lstrip(), where the argument is the set of chars
3. removeprefix will search for exact one match""")
print("*" * 83)
print("SYNTAX => String.removeprefix(substring)")
print("*" * 83)

name = "bala murugan "
name1 = "balabala murugan"
print(name.removeprefix("bla"))
print(name1.removeprefix("bala"))

word = "hubbubbubboo"
print(word.removeprefix("hub"))

print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.removeprefix)

# \n is an escape sequence to use ENTER
