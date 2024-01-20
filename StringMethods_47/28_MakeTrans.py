print("28. MAKETRANS")
# ref 48_Translate.py
print("*" * 83)
print(
    """1. Returns a translation table(dictionary) usable for translate() method
2.  This method takes 2 arguments(set of characters) which must be equal size
3. Each character from first argument will replace with each charater from\
 second argument
 4. The returned dictionary will contains ASCII value of character to be
 replace and replacing character as key-value pair
 5. Can also pass the mapping dictionary directly(1 argument) to get table
      """
)
print("*" * 83)
print("""SYNTAX => Str().maketrans(old,new)
Note: Here this method is called by string constructor, since no need for any
change in specific calling string""")
print("*" * 83)

table = str().maketrans("abc", "ABC")
print("ascii values of a,b,c are 97,98,99 which will replace by 65,66,67")
print(table)
print("type of the table : ", type(table))


print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.maketrans)
