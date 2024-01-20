print("40. SPLITLINES")
print("*" * 83)
print(
    """1. Split the string with linebreaks (\n)
2. Included the line breaker at end of each splitted string, if keepends=True
5. Returns list of strings of lines
"""
)
print("*" * 83)
print("SYNTAX => String.splitlines(keepends=False)")
print("*" * 83)


txt = """Hi
How are you
I am fine"""
print("Given String =>", txt)
print()
print("Splitlines()=>", txt.splitlines())
print("Splitlines(Keepends=True)=>", txt.splitlines(True))


print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.splitlines)
