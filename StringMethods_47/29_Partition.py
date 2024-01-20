print("29. PARTITION")
# ref 36_Rpartition.py for comparison
print("*" * 83)
print(
    """1. Partition the string into three parts using the given separator
2. If the separator is found-returns [BeforePart, Separator, AfterPart]
3. If the separator is not found-returns, original string and two empty strings
4. Search the separator occurrence from left
5. Returns tuple of size 3"""
)
print("*" * 83)
print("SYNTAX => String.partition(separator:str)")
print("*" * 83)

txt = "a+b=c=d"
print("Given string =>", txt)
print("Partition with '=' =>", txt.partition("="))
print("Partition with 'p' =>", txt.partition("p"))

print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.partition)

# \n is an escape sequence to use ENTER
