from f1 import Person
class Student(Person):
    def __init__(self, fname, lname, id):
        super().__init__(fname, lname)
        self.id = id

    def printname(self):
        print(self.firstname, self.lastname, self.id)
x = Student("George","Bush",7878)
x.printname()        