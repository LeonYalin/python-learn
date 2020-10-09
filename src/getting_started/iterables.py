from ..util import print_cmd


def using_comprehensions():
    print_cmd('Using comprehensions', """

    List compehensions:
    my_list = [len(x) for x in range(10)]

    Sets compehensions:
    my_set = {len(x) for x in range(10)}

    Dicts compehensions:
    my_new_dict = {key+2: val*val for key, val in my_list.items()}

    Filtering comprehensions
    my_lst = [x for x in range(101) if is_prime(x)]
    """)


def iteration_protocols():
    print_cmd('Iteration protocols', """
    There are 2 types of items iterable and iterator.
    Iterable can be passed to iter() to produce an iterator. Iterator can be passed to next() to get the next value.

    iterable = [1, 2, 3, 4]
    iterator = iter(iterable)
    next_value = next(iterator)

    Usage example:
    def first(iterable):
        iterator = iter(iterable)
        try:
            return next(iterator)
        except StopIteration:
            raise ValueError('iterable is empty')
    """)


def generator_functions():
    print_cmd('Generator functions', """
    Generator function is a function that evaluates values on demand, using the "yield" keyword. It returns iterator
    def gen_fun():
        yield 1
        yield 2
        yield 3
    g = gen_fun()
    print(g) # prints "<generator object gen_fun at 0x123ff1>"
    next(g) # prints 1
    next(g) # prints 2
    next(g) # prints 3
    next(g) # raises StopIteration error

    Complex example;
    def first(count, iterable):
        counter = 0
        for item in iterable
            if counter == count:
                return;
            counter += 1
            yield item

    def distinct(iterable):
        distinct_coll = set()
        for item in iterable:
            if not item in distinct_coll:
                yield item
                distinct_coll.add(item)

    def run_pipeline():
        items = [1, 3, 3, 6, 6, 2]
        for item in take(3, distinct(items)):
            print(item)

    We can force generator evaluation by wrapping it into list constructor, e.g. list(dictinct(items)).
    Because the evaluation is lazy, we can create very heavy loops without worring about memory consumption.

    Generator expressions:
    gen = (x*x for x in range(1, 1000001)) # million squares calulation. No memory usag, cause no calculations made (lazy evaluation) 
    We can do sum(x*x for x in range(1, 1000001) if is_primt(x)) and omit pair of parenthesses needed for sum.
    """)


def iterable_tools():
    print_cmd('Iterable tools', """
    Python has the built-in "itertools" package for forking with iterables.

    itertools.islice(iter, 100) - lazy slicing of any iterator
    itertools.count() - lazy version of range(), yields infinite sequence
    Example:
    thousand_primes_gen = islice(x for x in count() if is_prime(x), 1000)

    itertools.any([False, True, False]) - returns true if finds any boolean expression that is true
    itertools.all([False, True, False]) - returns true if all boolean expressions are true
    Example:
    any_primes_in_range = any(is_prime(x) for x in range(1201, 1221))
    all_uppercase = all(name == name.title() for name in ['Tel Aviv', 'B7', 'Ashdod'])

    itertools.zip(...iterables) - synchronize iteration between two iterables, produces a tuple
    Example:
    leon_grades = [56, 79, 80, 95]
    nelly_grades = [9, 23, 46, 87]
    for leon_grade, nelly_grade in zip(leon_grades, nelly_grades):
        print('average grade = ', (leon_grade + nelly_grade) / 2)

    itertools.chain(...iterables) - concats iterables into one sequence
    Example:
    all_positive = all(x > o for chain([1, 2, 3], [23, 456, 76], [11, 34545, 8]))
    """)

def iterables_main():
    using_comprehensions()
    iteration_protocols()
    generator_functions()
    iterable_tools()