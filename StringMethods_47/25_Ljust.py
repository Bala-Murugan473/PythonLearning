print("25. LJUST")
# inverse to rjust(), ref 35_Rjust.py
print("*" * 83)
print(
    """1.  Return a left-justified string of given width
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

print(name.ljust(10, "_"))
print(name2.ljust(10, "_"))

print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.ljust)

# \n is an escape sequence to use ENTER
