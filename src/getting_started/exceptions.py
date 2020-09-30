from ..util import print_cmd


def handling_exceptions():
    print_cmd('Handling exceptions', """
    The try-catch blocks in python are represented as try/except blocks, e.g.
    try:
        a = 'aaa'
        b = {'b', 'bb'}
        int(a) # TypeError
        b['c'] # KeyError
    except KeyError:
        print('Key is not valid!')
    except TypeError:
        print('Type is not valid!')
    except(ImportError, IndexError): # Can be tuple as well
        print('multiple errors handler')
    except(IndentationError, SynthaxError, NameError) as e: # Programmer errors
        print(e, file=sys.stderr)
        pass # a no-op
    finally:
        print('do some cleanup here')
    
    To raise an exception, use the "raise" keyword. Use raise inside exception to re-raise it.
    if (3 / 0):
        raise ValueError('cannot divide by 0')

    Common exception types:
    - IndexError: index out of range
    - ValueError: invalid value, e.g. int("asd")
    - KeyError: key does not exist

    There are two conceptual ways to handle exceptions:
    - LBYL: "Look Before You Leap" -> perform checks and validations before run
    - EAFP: "Easier To Ask Forgiveness Than Permission" -> run and be prepared for exceptions
    """)

def exceptions_main():
    handling_exceptions()