print("45_TRANSLATE")
# ref 28_MakeTrans.py
print("*" * 83)
print(
    """1. Replace each character in the string by given translation table
2.  The translation table can be create using maketrans() method"""
)
print("*" * 83)
print("SYNTAX => Str().translate(translation_table)")
print("*" * 83)

table = str().maketrans("abc", "ABC")
txt = "balamurugan"
print("Given String <=", txt)
print("Translated String =>", txt.translate(table))

print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.translate)
