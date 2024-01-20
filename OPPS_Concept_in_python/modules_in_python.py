# A module is nothing but a python file.
# The file name is the module name with suffix .py appended
# A module is a file containing python definitions and statements

# A module can contain executable statements as well as function definitions.
# These executable statements are indented to initialize the module.
# they are execute only the first time the module is encountered in an import statement.

# With in a module, the module's name is available in variable __name__ is global namespace

# To use a module, import module name
import sys

# When importing a module, it doesn't add the names of the functions defined in the module directly to current namespace
# instead, it only adds the module name to the current namespace.

from math import gamma

# The above syntax only imports the module member alone from the module, instead of importing the whole module.

import math as m
from math import gamma as g

# If the module name is big, we can use alias 'as'

# Note: each module is only imported once per interpreter session.
# If you change module, restart the interpreter.


# MODULE SEARCH PATH:

# When a module is imported, the interpreter first searches for a buin-in module with that name.
# These built-in modules are listed in sys.builtin_module_names
# If not found, it searches for a file with that name in a list of directories given by the variable sys.path
print(sys.path)

# sys.path is initialized from these locations,
# # directory containing the input file.( or current directory, when no file is specified.
# # python path
# # site-packages directory

