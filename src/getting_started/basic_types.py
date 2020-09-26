def creating_integers():
    print("""
  Creating integers:
  - 10 -> 10 (regular)
  - 0b10 -> 2 (binary)
  - 0o10 -> 8 (oktal)
  - 0x10 -> 16 (hex)
  - int(3.5) -> 3, int("123") -> 123 (parseInt)
  """)


def creating_floats():
    print("""
    Creating floats:
    - 3.125 -> 3.125 (regular)
    - 3e8 -> 3000000008.0 (big)
    - 1.616e-35 -> 1.616e-35 (small)
    - float(7) -> 7.0, float("1.23") -> 1.23 (parseFloat)
    - float("nan") -> nan, float("inf") -> inf, float("-inf") -> -inf
    """)


def creating_other_types():
    print("""
    Creating other types:
    - None, a = None, a is None (Null)
    - bool, a = False, bool(0) -> False, bool(1) -> True, bool("") -> False, bool([]) -> False, bool("False") -> True, bool("True") -> True
    """)


def using_relational_operators():
    print("""
    The relational operators in Python are:
    ==, !=, <, >, <=, >=, -=, +=, *=, /=
    """)


def using_if_else_blocks():
    print("""
    Using the if/else blocks:
    a = 2
    if a == 2:
        print("lala")
    elif a > 3:
        print("mama")
    else:
        print("lulu")
    """)


def using_for_loops():
    print("""
    Using for loops:
    arr = [1, 2, 3]
    for num in arr:
        print(num) -> 1, 2, 3
    obj = {'a': 'aaa', 'b': 'bbb'}
    for key in obj:
        print(key, obj[key]) -> 'a, 'aaa', 'b', 'bbb'
    """)


def using_while_loops():
    print("""
    Using the while loops:
    a = 5
    while a > 0:
        response = input() # user input from keyboard
        if response == 1:
            break
        a -= 1
    """)


def using_strings():
    print("""
    Using strings:
    - string literals: "aaa" or 'aaa'
    - multiline strings: '''multiline strings''' or "multiline\n strings\n"
    - raw strings: path = r'C:\Games\Heroes7' -> r"C:\\Games\\Heroes7"
    - get string chars: a = "aaa", a[0] -> a, type(a[0]) -> 'class str'
    - convert to string: str(123) -> "123" (toSting
    - type help(str) to get the list of all avaliable string methods
    """)


def using_bytes():
    print("""
    Using bytes:
    - create: a = b'bytes data'
    - split: a.split(" ") -> [b'bytes', b'data']
    - encode: str = "привет".encode("UTF-8") -> b'\xd0\xbf...'
    - decode str.decode('UTF-8) -> "привет"
    """)


def using_lists():
    print("""
    Using lists:
    a = [1, 2, 3] -> [1, 2, 3], a[1] -> 2, a[1] = "orange" -> [1, "orange", 3]
    list('abc') -> ['a', 'b', 'c']
    arr = [ 'a',
            'b',
            'c',]
    """)


def using_dicts():
    print("""
    Using dictionaries:
    - d = {}, d = {'a': 'aaa', 'b': 'bbb'}, b['a'] -> 'aaa', b['a'] = 'ccc'
    """)


def putting_it_all_together():
    words = []
    with open('./words.txt',  encoding="utf-8") as f:
        for row in f:
            for word in row.split():
                words.append(word)
    print(words)


def basic_types_main():
    creating_integers()
    creating_floats()
    creating_other_types()
    using_relational_operators()
    using_if_else_blocks()
    using_while_loops()
    using_strings()
    using_bytes()
    using_lists()
    using_dicts()
    putting_it_all_together()
