from abc import ABCMeta, abstractclassmethod

class IPerson(metaclass=ABCMeta):
    @abstractclassmethod
    def person_method():
        """Interface Method"""

class Student(IPerson):

    def __init__(self) -> None:
        self.name = "Basic student name"

    def person_method(self):
        """Implementation of the person_method for Student"""
        print("I am a student")

class Teacher(IPerson):

    def __init__(self) -> None:
        self.name = "Basic teacher name"

    def person_method(self):
        """Implementation of the person_method for Teacher"""
        print("I am a teacher")


class PersonFactory:

    @staticmethod
    def build_person(person_type : str):
        """Static method to create instances of Student or Teacher based on input"""
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        print("Invalid Type")
        return -1
    
if __name__ == "__main__":
    choice = input("What type of person do you want to create?\n")
    person = PersonFactory.build_person(choice)
    person.person_method()  # Call the person_method of the created person
