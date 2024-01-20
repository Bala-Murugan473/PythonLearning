""" Return a formatted version of S, using substitutions from mapping. """
""" The substitutions are identified by braces ('{' and '}'). """

help(str.format_map)

coordinates: dict = {"x": 10, "y": 20}  # ,mapping substitution
txt = "the cordinate of x is {x} and y is {y}"
txt1 = "the cordinate of y is {y} and x is {x}"
print(txt.format_map(coordinates))
print(txt1.format_map(coordinates))
