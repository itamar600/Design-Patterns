from abc import ABCMeta, abstractmethod

class IPerson(metaclass=ABCMeta):
    @abstractmethod
    def person_method():
        """Interface Method"""

class Person(IPerson):
    """
    Concrete implementation of IPerson representing a person.
    """
    def person_method(self):
        """Method to describe a person."""
        print("I am a person")

class ProxyPerson(IPerson):
    """
    Proxy class for Person, adding additional functionality.
    """
    def __init__(self) -> None:
        self.person = Person()  # Instantiating a Person object

    def person_method(self):
        """Method to provide proxy functionality."""
        print("I am the proxy functionality")
        self.person.person_method()  # Calling the person_method of the Person object

# Creating a Person object and calling person_method
p1 = Person()
p1.person_method()

# Creating a ProxyPerson object and calling person_method
p2 = ProxyPerson()
p2.person_method()
