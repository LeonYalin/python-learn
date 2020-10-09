from ..util import print_cmd
from .models.person import printPersonWithAddress


def using_classes():
    print_cmd('Using classes', """
    Creating classes:

    class EmptyClass:
        pass
    

    person = Person('Leon',  'Yalin') # self argument not provided
    person.full_name() #
    # above is a sintactic sugar for Person.full_name(f)

    Look on the person.py class implementation to continue

    Polymorphism in Python is achieved thought Duck Typing, that is a principle in Python
    """)
    printPersonWithAddress()


def classes_main():
    using_classes()