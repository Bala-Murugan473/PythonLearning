print("7. EXPANDTABS")
print("*" * 83)
print(
    """1. Used to Replace the tab with given number of spaces
2. If tab size is not given, a tab size of 8 characters is assumed
3. Returns new string, doesn't change the original string"""
)
print("*" * 83)
print("SYNTAX => String.expandtabs(tabsize: int)")
print("*" * 83)

txt = "Basic\tpython"
print("Given String <=", txt)
print("Expandedtab with size '12' =>", txt.expandtabs(12))
print("Expandedtab with size '20' =>", txt.expandtabs(20))

print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.expandtabs)

# \t is an escape sequence to use TAB
# \n is an escape sequence to use ENTER
