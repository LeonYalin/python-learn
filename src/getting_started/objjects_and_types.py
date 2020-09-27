def values_and_identity_equality():
  print("""
  Using identifiers:
  - id is a unique identifier that every object in Python has (like pointer - memory address) 
  a = 16
  b = 'bbb'
  id(a) -> 4301474256
  id(b) -> 2548596870
  a = b -> a -> b -> 2548596870
  a is b -> True, or id(a) == id(b)

  Value vs identity equality:
  a = [1, 2, 3]
  b = [1, 2, 3]
  a == b -> True (value equality)
  a is b -> False (identity equality)
  """)


def using_function_arguments():
    print("""
    Using function arguments:
    - default arguments
    foo(word, multiplier = 2):
        print(len(work) * 2) -> len(word) will give the word length
    --> foo("Hello")
    --> foo("Hello", 5) - order is important
    --> foo(word="Hello", multiplier=3), or foo(multiplier=3, word="Hello") - any order
    --> foo("Hello", multiplier=5) - can be combined
    This is called "keyword arguments", and they must come after positioned arguments
    """)


def using_default_values():
    print("""
    Using default values:
    - The default values are created only once and are mutable. Therefore, using the following will get surprising results:
    def addToList(list = []):
        list.append("lala")
        return list
    --> addToList() -> ['lala']
    --> addToList() -> ['lala', 'lala']
    To fix this, use only integers, strings or None as default parameters
        def addToList(list = None):
            if list == None:
                list = []
        list.append("lala")
        return list
    """)

def using_scopes():
    print("""
    Using scopes:
    In python, there are 4 scopes:
    - Local -> inside the function
    - Enclosing -> inside enclosing function
    - Global -> At the top level of the module
    - Built-in -> In the special Built-ins module
    Together, they for the "LEGB" rule.
    Scopes do not correspond to the code blocks and indentation (like in JavaScript)

    There are collitions between local and global variables with same name. For example:
    count = 0
    def set_count(num)
        count = num
    set_count(5)
    print(count) -> prints 0, because it implicitly creates local "count" variable and assigned 5 to it

    To solve this, use the "global" keyword
    def set_count(num)
        global count
        count = num
    """)


def inspecting_objects():
    print("""
    To inspect an object, we can use som built-in commands:
    import module_name
    type(module_name) -> <class 'module'>
    dir (module_name) -> will show object attributes, such as properties and methods
    - __name__ can be used to get the function name
    - __doc__ can be used to get the function docstring 
    """)


def objects_and_types_main():
  values_and_identity_equality()
  using_function_arguments()
  using_default_values()
  using_scopes()
  inspecting_objects()

