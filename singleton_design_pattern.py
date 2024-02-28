from abc import ABCMeta, abstractmethod

class IPerson(metaclass=ABCMeta):
    """
    Abstract base class defining the interface for a person.
    """
    @abstractmethod
    def print_data():
        """Abstract method to print person data."""
        pass

class PersonSingleton(IPerson):
    """
    Singleton class implementing the IPerson interface.
    """
    __instance = None  # Private class variable to hold the singleton instance

    @staticmethod
    def get_instance():
        """
        Static method to get the singleton instance.

        Returns:
            PersonSingleton: The singleton instance.
        """
        if PersonSingleton.__instance == None:
            PersonSingleton("Default Name", 0)
        return PersonSingleton.__instance
    
    def __init__(self, name, age):
        """
        Constructor to initialize the singleton instance.

        Args:
            name (str): Name of the person.
            age (int): Age of the person.
        """
        if PersonSingleton.__instance != None:
            raise Exception("Singleton cannot be instantiated more than once!")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self
    
    @staticmethod
    def print_data():
        """Static method to print person data."""
        print(f"Name: {PersonSingleton.__instance.name}, Age: {PersonSingleton.__instance.age}")

# Creating an instance of PersonSingleton
p = PersonSingleton("Mike", 30)
print(p)  # Printing the instance
p.print_data()  # Printing person data

# Trying to create another instance of PersonSingleton (should raise an exception)
p1 = PersonSingleton("Mike", 30)

# Getting the singleton instance using get_instance method
p2 = PersonSingleton.get_instance()
print(p2)  # Printing the singleton instance
p2.print_data()  # Printing person data
