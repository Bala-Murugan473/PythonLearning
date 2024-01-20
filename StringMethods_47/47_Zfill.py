print("47. ZFILL")
print("*" * 83)
print(
    """1.  Return a right-justified string of given width
2. If the length of the given string is less than the mentioned length, then
'0' will filled before the string to get the required string length
3. If string length is greater than the fill length , then no effect"""
)
print("*" * 83)
print("SYNTAX => String.zfill(width : int)")
print("*" * 83)

name = "bala"
name2 = "BalamuruganBasicPython"
name3 = "+bala"
name4 = "$bala"

print(name.zfill(10))
print(name2.zfill(10))

print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.zfill)

# \n is an escape sequence to use ENTER
print("47. ZFILL")
print("*" * 83)
print(
    """1.  Return a right-justified string of given width
2. If the length of the given string is less than the mentioned length, then
'0' will filled before the string to get the required string length
3. If string length is greater than the fill length , then no effect
4. If any sign (+ or -) present at the begining of the string, then zeros will\
filled inbetween sign and strings"""
)
print("*" * 83)
print("SYNTAX => String.zfill(width : int)")
print("*" * 83)

name1 = "bala"
name2 = "BalamuruganBasicPython"
name3 = "+bala"
name4 = "$bala"

print(name1, ": zfill(10) =>", name1.zfill(10))
print(name2, ": zfill(10) =>", name2.zfill(10))
print(name3, ": zfill(10) =>", name3.zfill(10))
print(name4, ": zfill(10) =>", name4.zfill(10))

print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.zfill)

# \n is an escape sequence to use ENTER
