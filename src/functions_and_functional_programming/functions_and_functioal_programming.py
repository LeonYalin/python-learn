from ..util import print_cmd


def functions_and_callables():
    print_cmd('Functions and callables', """
    Callable instances:
    To make an instance callable, we must implement the __call__ method in the class. For example, 
    class Person:
        def __call__():
            print('lala')

    leon_yalin = Person()
    leon_yalin() # prints 'lala'

    # The above is the synthactic sugar for the following:
    leon_yalin.__call__() # 

    One more example of the callables feature:
    def sequence_cls(immutable):
        return tuple if immutable else list

    cls = sequence_cls(False)
    cls('Leon') # prints ['L', 'e', 'o', 'n']

    Lambdas:
    Lambdas are anonimous functions and can be used with callables. Lambd has the form "lambda arge: expr".
    sorted(['b_2', a_1'], key=lambda name: name.split('-')[-1]) # prints ['a_1', 'b_2']

    To determine, is something is callable, we simply pass it to the callable(var) function, which returns True or False
    functions are callable, lambdas are callable, classes are callable, collections are callable 
    """)


def extended_argument_and_call_syntax():
    print_cmd('Extended argument and call syntax', """
    Using multiple arguments:

    For positioned arguments:
    def foo(*args):
        print(args)

    This is called "star arguments", its type is typle
    To avoid the no arguments error, we can modify the function as follows:
    def foo(arg, *args):
        pass

    Here, if we iterate over values, no StopIteration error with e raised.

    For keyword arguments:
    def foo(**kwargs)

    This is called "keyword arguments", its type is dict.

    We can combine the positional and keyword arguments, but the order is important:
    def foo(arg1, arg2, *args, kwarg1, kwarg2, **kwargs):
        pass

    We can allow only spacific number of positioned arguments using this syntax:
    def foo(arg1, arg2, *, kwarg1):
        pass

    We can force the function to have positional arguments only by using this syntax: (Python 3.8+ only)
    def foo(arg1, /):
        pass

    Extended call syntax: (a.k.a. spread operator in JavaScript)
        def foo(arg1, arg2, *args, **kwargs):
            pass

        positional_args_tuple = (12, 23, 456, 667)
        keyword_args_dict = {'a', 'a', 'b': 'b'}
        foo(*positional_args_tuple, **keyword_args_dict) # used like the Spread operator in JavaScript
    """)


def closures():
    print_cmd('Closures', """
    
    """)


def functions_and_functional_programming_main():
    functions_and_callables()
    extended_argument_and_call_syntax()
    closures()