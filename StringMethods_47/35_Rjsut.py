print("35. RJUST")
# inverse to ljust(), ref 25_Ljust.py
print("*" * 83)
print(
    """1.  Return a right-justified string of given width
2. If the length of the given string is less than the mentioned length then
the assigned char will place for the remaining chars
3. Default char is space' ', the paramter should be char not string
4. If string length is greater than the justify length , then no effect"""
)
print("*" * 83)
print("SYNTAX => String.ljust(width : int, filling_character)")
print("*" * 83)

name = "bala"
name2 = "BalamuruganBasicPython"

print(name.rjust(10, "_"))
print(name2.rjust(10, "_"))

print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.rjust)

# \n is an escape sequence to use ENTER
