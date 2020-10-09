"""Person classes and functions"""

class Person:
    """Model for a person."""


    def __init__(self, first_name, last_name, address):
        """__init__ is not a constructor, but an initializer (a.k.a ngOnInit() in Angular)"""


        # CLass invariants (Checks that should be applied before we do comething with the instance)

        if not first_name.isalpha() or not last_name.isalpha():
            raise ValueError(f'{first_name} and {last_name} should be strings')

        if not first_name[:1].isupper() or not last_name[:1].isupper():
            raise ValueError(f'First letter in {first_name} or {last_name} should be capitalized')
        

        self._first_name = first_name
        self._last_name = last_name
        self._address = address


    def full_name(self):
        return f'{self._first_name} {self._last_name}'

    def full_address(self):
        return f'{self._address.city}, {self._address.street} {self._address.ap_num}'


class Address:
    """ Model for an address"""


    def __init__(self, city, street, ap_num):
        self.city = city
        self.street = street
        self.ap_num = ap_num


class Student(Person):
    """Student derived from Person - has a average grade"""


    def __init__(self, avg_grade):
        self._avg_grade = avg_grade

    def full_name(self):
        """Calling methon full_name of the parent"""
        return f'{Person.full_name(self)},avg_grade={self._avg_grade}'



def printPersonWithAddress():
    person = Person('Leon', 'Yalin', Address('Petach Tikva', 'Tsahal', '10'))
    print(f'Person[full_name={person.full_name()}], full_address={person.full_address()}')