# !/usr/bin/python  # -*- coding: latin-1 -*-
print("5. ENCODE\n" + "*" * 83)
print(
    """1. Encode the given string using the specified encoder
2. If no encoding is specified, UTF-8 will be used
3. Errors is an optional parameter->read help printed last
3. Returns new string, doesn't change the original string"""
)

print("*" * 83)
print("""SYNTAX => String.encode(encoding ,errors='strict')""")
print("*" * 83)

txt = "B�sic Python"
# if no encoding char found, error='strict' will throw error
strict = txt.encode(encoding="UTF-8", errors="strict")
backslashreplace = txt.encode(encoding="ascii", errors="backslashreplace")
ignore = txt.encode(encoding="ascii", errors="ignore")
namereplace = txt.encode(encoding="ascii", errors="namereplace")
xml = txt.encode(encoding="ascii", errors="xmlcharrefreplace")

print("Given String \t\t<=", txt)
print("UTF-8, strict \t\t=>", strict)
print("ASCII, blackslashreplace =>", backslashreplace)
print("ASCII, ignore \t\t=>", ignore)
print("ASCII, namereplace \t=>", namereplace)
print("ASCII, xmlcharrefreplace =>", xml)


print("*" * 83 + "\n\n****** BUILT IN DOC ******")
help(str.encode)
