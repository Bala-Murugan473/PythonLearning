# The __init__.py is required to make python treat directories containing the file as package.
# __init__.py is an empty file sometimes.( if it is empty, it only import top level packages & names in it.

# Usage: import toplevel_package.subpackage.file

# when using the syntax, import item.subitem.subsubitem, each item except the last must be a package.
# the last item can be a module or package, but cannot be a class or function or variable defined in the previous item

# import statement first test whether the item is defined in  the current package.
# if not, it assumes it as a module and attempts to load it.


# from package import subitem

# When using from package import item , the item can be either a submodule (or subpackage)
# of the package, or some other name defined in the package like class, function or variable.
