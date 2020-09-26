def using_dunders():
    print("""
  Using dunders:
  - dunder is a shortcut for pronouncing properties like __name__, and stands for: double underscore
  - using dunder __name__ will print the target that is calling the script.
  - When imported as a module, print(__name__) will print the module name, when called from cmd, will print "__main__"
  - That's why we can reference this and create a "main" like method:

  if __name__ == "__main__":
    main()
  """)


def using_cmd_args():
    print("""
    Using command line arguments:
    - import sys
    - sys.argv(1) to get the first argument
    """)


def using_docstrings():
    print("""
    Using docstrings:
    - Docstrings is like JavaDoc, and it is used as a documentation for methods or modules.
    - The docstring should be written using '''docstring here''' in the first line of the method or module.
    - Then, we can acsess them by typing help(module_name) or help(method).
    """)


def using_comments_and_shebangs():
    print("""
    Using comments:
    - # this is a comment, both for single and multiline comments
    - shebang indicates, which program should be run the file with, e.g.
    - #!/usr/bin/env python3, or #!/bin/bash
    """)

def modularity_main():
    using_dunders()
    using_cmd_args()
    using_docstrings()
    using_comments_and_shebangs()
