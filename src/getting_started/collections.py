from ..util import print_cmd


def tuples():
    print_cmd('Using tuples', """
    Tuples are sequences of odrinary objects. We can create a tuple with a couple of ways:
    - tuple([123, 34, "asd"])
    - a = ("aaa", 23, 34.5)
    - a[0] -> "aaa"
    - len(t) -> 3
    - aa = ((11, "12"), (22, "23"))
    - aa[1[1]] -> "23"
    - b = (234,) # trailing comma is a must, otherwise the compiler will transform it to int
    - c = () # emply tuple 
    - d = 1, 2, 3, "asd" # we can omit parentheses

    Looping and concatinating tuples:
    for item in a:
        print(item)
    - a + (123, "bbb") -> ("aaa", 23, 34.5, 123, "bbb")

    Tuple unpacking (destructuring):
    def minmax(items):
        return min(items), max(items)
    min, max = minmax([1, 2, 3, 4])


    Swap item using tuple unpacking:
    a = 123
    b = "aaa"
    a, b = b, a

    Check if tuple contains specific value:
    5 in (1, 2, 435, 5)
    4 not in (1, 2, 345)
    """)


def strings():
    print_cmd('Using strings', """
    Creating a string:
    - "lala", len("lala") -> 4
    - "a" + "b" + "c", or a += "bc"
    
    Preferred way of contanenating strings is join, which is more efficient
    word = '-'.join('a', 'b', 'c') # produces "a-b-c"
    word.split("-")

    String partitioning:
    "unforgetable".partition('forget') # returns tuple ('un'm 'forget', 'able')
    id, name = '12345:leon'.partition(':') # use together with unpacking


    Formatting strings:
    'My name is {0} {1}'.format('Leon', 'Yalin')
    'My name is {name} {surname}'.format(name='Leon', surname='Yalin') # using named parameters
    'Math constants: pi={m.pi:.3f}, e={m.e:.2f}'.format(m=math) # using modules and precition 
    f'Math constants: pi={math.pi:.3f}, e={math.e:.2f}' # the new way to format, also called as f' strings
    """)


def ranges():
    print_cmd('Using ranges', """
    for i in range(5):
        print i # will print "0, 1, 2, 3, 4"
    range(5, 10) # will print "5, 6, 7, 8, 9"
    range(0, 10, 2) # will print 0, 2, 4, 6, 8
    list(range(5, 10)) # will create a list of [5, 6, 7, 8, 9]

    for tp in [123, 456, 78]:
        print(tp) # will print (0, 123), (1, 456), (2, 78)

    If we need to use indexs in loops, use the enumerate() function:
    for i, v in enumerate([123, 456, 78]): # use unpacking for readability
        print(i, v)
    """)


def lists():
    print_cmd('Using lists', """
    l = [123, 456, 78]

    Using negative indeses
    l[-1] # gives 78
    l[-2] # gives 456
    l[-0] # gives 123

    Slicing lists:
    l = [12, 34, 56, 78, 9]
    l[1:3] # will give 1-st to 3-rd list item (non-inclusive): [34, 56]
    l[1:-1] # 1-st to last list item (non-inclusive): [34, 56, 78]
    l[2:] # from 2-nd item and all next: [56, 78, 9]
    l[:2] # up until 2-nd item (non-inclusive): [12, 23]
    l[:] # all range. used to copy a list: [12, 34, 56, 78, 9]. Comparing "l is [12, 34, 56, 78, 9]" -> False

    Other ways to copy a list:
    l_copy = l.copy()
    l_copy2 = list(l)
    l is l_copy -> False, l is l_copy2 -> False
    - All these perform a shallow copy of a list. To make a deep copy, use a "copy" module from the core os.

    Creating lists with repetition:
    [0] * 9 # will create [0, 0 ,0, 0, 0, 0, 0, 0, 0]
    [[1, 2]] * 3 # will create [[1, 2], [1, 2], [1, 2]] but with only references. Modifiying one will modify the others!

    Finding elements:
    ['a', 'b', 'c'].index('a') # will uotput 0
    ['a', 'b', 'c'].index('abc') # will produce ValueError
    - To find without erros, use "in": 'a' in ['a', 'b', 'c'], 'd' not in ['a', 'b', 'c'] 

    Removing elements:
    a = ['a', 'b', 'c'] 
    del a[0] # ['b', 'c']
    a.remove('a') # alternative method

    Inserting elements:
    ['a', 'b', 'c'].insert(1, 'aaa') # ['a', 'aaa', 'b', 'c']
    ['a', 'b', 'c'].append('d') # ['a', 'b', 'c', 'd']

    Concatenating lists:
    a = ['a', 'aa', 'aaa']
    b = ['b', 'bb']
    c = a + b # ['a', 'aa', 'aaa', 'b', 'bb']
    d += ['c'] # ['a', 'aa', 'aaa', 'b', 'bb', 'c']
    d.extend(['d', 'dd']) # ['a', 'aa', 'aaa', 'b', 'bb', 'c', 'd', 'd']

    Reversing a list:
    a = ['a', 'aa', 'aaa']
    a.reverse() # ['aaa', 'aa', 'a']

    Sorting a list:
    a = [2, 1, 3]
    a.sort() # [1, 2, 3]
    a.sort(reverse=True) # [3, 2, 1]
    ['aa', 'a', 'aaa'].sort(key=len) # ['a', 'aa', 'aaa'],sorts by passing a callable argument to key (e.g. function len)
    - To sort and reverse list in immutable way, use reversed() and sorted() functions that return iterators
    """)


def dicts():
    print_cmd('Using dicts', """
    Creating a dict:
    a = {'a': 'aaa'} # a['a'] -> 'aaa'
    b = dict([('a', 'aa'), ('b', 'bb')]) # {'a': 'aa', 'b': 'bb'}
    c = dict(a='aa', b='bb') # using named arguments

    Copying a dict:
    copy = d.copy()
    copy2 = dict(other_dict)

    Merging dicts:
    d.update(another_dict)

    Iterating over dicts:
    for key in my_dict:
        print(key, my_dict[key])

    for key in my_dict.keys():
        print(key, my_dict[key])

    for value in my_dict.values():
        print(value)

    for key, value in my_dict.items():
        print(key, value)

    Finding key in dict:
    'aaa' in my_dict
    'aaa' not in my_dict

    Deleting a key from dict
    del my_dict['a']

    Printing a dict:
    from pprint import pprint as pp
    pp(my_dict)
    """)


def sets():
    print_cmd('Using sets', """
    Creating a set:

    s = {23, 345, 1, 2}
    s2 = set([23, 345, 1, 2, 2, 1]) # removes duplicates in constructor

    Finding an element in set:
    1 in my_set
    23 not in my_set

    Adding an element to set:
    my_set.add(123)

    Deleting an element from set:
    my_set.remove(123) # an Error is thrown if element is not present
    my_set.discard(12) # no errors if element not present

    Copying a set (shallow copy):
    copy = my_set.copy()
    copy2 = set(my_set)

    Useful set methods (Algebra):
    a.union(b) # all a and b
    a.intersection(b) # only a and b common part  
    a.difference(b) # only a and not b
    a.symmetric_difference(b) # both a and b parts that are not common
    a.issubset(b) # all a elements are inside b
    a.issuperset(b) # all b elements are inside a
    a.isdisjoint(b) # no common elements
    """)


def protocols():
    print_cmd('Using protocols', """
    Protocols is like interfaces, but we don't need to write "implements ___", only implement the methods
    Common protocols in Python are:
    - Container (in, not in)
    - Sized (len)
    - Iterable (for .. in)
    - Sequence (var[index])
    """)


def collections_main():
    tuples()
    strings()
    ranges()
    lists()
    dicts()
    sets()
    protocols()